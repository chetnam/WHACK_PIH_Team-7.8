from flask import Flask, request, redirect
from flask import render_template
from twilio import twiml
from orderValidity import *

app = Flask(__name__)

import db_model as db
import json

from datetime import date
from datetime import timedelta

messageInfo = dict()

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        request.form
    return render_template("index.html")


   # results = db.select_one()
   # typeOfQuery = request.form['order']
   # # location = request.form['location']
   # # item = request.form['item']
   # message = messageInfo #dictionary of location_id, sku, itemAmount, dateSent
   #
   # return render_template("index.html")


#replies to user's text
@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
   """Send a dynamic reply to an incoming text message"""
   # Get the message the user sent our Twilio number
   #body = client.messages.get('+16303625933')
   body = request.get['Body']
   date = request.get['DateSent']
   validMessage = isBodyValid(body)

   # Start our TwiML response
   response = twiml.Response()

   message = '';

   # Determine the right reply for this message
   # Text Message should be in form "Location_ID, SKU, ItemAmount"
   if validMessage==True:
       parsedMessage = splitBody(body)
       message = "Location " + parsedMessage["location_ID"] + " , thank you for your order!"
       parsedMessage['Date'] = date
       messageInfo = parsedMessage
       #db.add(parsedMessage)
   elif validMessage!=True:
       message = "Please abide by the order message syntax rules and try again. Thank yoU!"

   response.sms(message)
   return str(response)

if __name__ == "__main__":
   app.run('0.0.0.0')
