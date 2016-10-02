"""
    Connect to a vertica database and run queries
"""
from flask import g
import vertica_python

import re
import os
import datetime

DB_NAME = 'test'
DB_USER = 'dbadmin'
DB_PASSWORD = ''
DB_HOST = 'ec2-54-210-236-166.compute-1.amazonaws.com'

conn_info = {'host': DB_HOST,
             'port': 5433,
             'user': 'dbadmin',
             'password': '',
             'database': 'test',
             # 10 minutes timeout on queries
             'read_timeout': 600,
             # default throw error on invalid UTF-8 results
             'unicode_error': 'strict',
             # SSL is disabled by default
             'ssl': False}

def make_dicts(cursor, row):
    """
        Turn query results into dictionaries keyed by column name
    """
    colnames = [col[0] for col in cursor.description]

    fmtrow = {}
    for idx, value in enumerate(row):
      fmtrow[colnames[idx]] = value

    return fmtrow

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = vertica_python.connect(**conn_info)
    return db


def query_db(query, args=(), one=False):
    print query
    cur = get_db().cursor()

    try:
        cur.execute(query, args)
        rv = cur.fetchall()

        # Turn into colname->val dict representation of tuple
        # this isn't very efficient but will suffice for now
        rv = [make_dicts(cur, row) for row in rv]
    except Exception, e:
        print e
        rv = [{'error': e}]

    cur.close()
    return (rv[0] if rv else None) if one else rv


def addOrder(m):
    query_db("insert into orders (sku, location_id, item_amount, date_received) values ('" + str(m['SKU']) + "'," + str(m['location_id']) + "," + str(m['amount']) + ",'" + str(datetime.datetime.now()) + "'::timestamp); commit;")

def getOrders():
    return query_db("select * from orders;")

# pls only run once to setup the tables
def setup():
    cur = get_db().cursor()
    # create_pih_table = "create table pih_supply( \
    #                     sku char(4) not null primary key, \
    #                     name varchar(100), \
    #                     category varchar(100), \
    #                     unit_of_measure varchar(10), \
    #                     manufacturer varchar(100), \
    #                     brand varchar(100), \
    #                     manufacturer_code varchar(50), \
    #                     manufacturer_name varchar(200), \
    #                     vendor varchar(100), \
    #                     vendor_code varchar(50), \
    #                     vendor_name varchar(100), \
    #                     cold_chain enum('TRUE', 'FALSE'), \
    #                     UPC varchar(50), \
    #                     NDC varchar(50), \
    #                     );"

    try:
        with open("pih_data.tsv") as f:
            count = 0
            for l in f:
                if count > 0:
                    d = l.strip().split('\t')
                    row_query = "insert into pih_data values (" + "'" + d[0].replace("'",'') + "','" + d[1].replace("'",'') + "','" + d[2].replace("'",'') + "','" + d[3].replace("'",'') + "','" + d[4].replace("'",'') + "','" + d[5].replace("'",'') + "','" + d[6].replace("'",'') + "','" + d[7].replace("'",'') + "'," + "'" + d[8].replace("'",'') + "'," + "'" + d[9].replace("'",'') + "'," + "'" + d[10].replace("'",'') + "'," + "'" + d[11].replace("'",'') + "'); commit;"
                    cur.execute(row_query)
                    print row_query
                count += 1

        # rv = cur.fetchall()

        # Turn into colname->val dict representation of tuple
        # this isn't very efficient but will suffice for now
        # rv = [make_dicts(cur, row) for row in rv]
    except Exception, e:
        print e
        # rv = [{'error': e}]


    cur.close()

def select():
    """
        Select 1 from database
    """
    sql = "SELECT * FROM pih_data"
    results = query_db(sql)

    return results

# @app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
