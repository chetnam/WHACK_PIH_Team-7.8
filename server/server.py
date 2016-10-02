from flask import Flask, request, redirect
from flask import render_template
#twiml
from twilio import twiml

app = Flask(__name__)

import db_model as db
import json

from datetime import date
from datetime import timedelta

lastMessage = None

@app.route("/")
def index():

    results = db.select_one()

    return render_template("index.html", lastMessage=lastMessage)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    
    print request.method


    if request.method == 'POST':

        print request.values

        body = request.values.get('Body', None)

        # Start our TwiML response
        resp = twiml.Response()

        # Determine the right reply for this message
        if body == 'hello':
            resp.message("Hi!!")
            resp.sms("Hi!")
        elif body == 'bye':
            resp.message("Goodbye")
        else:
            resp.message("  asdgasdg ")
            resp.sms("YO")

        global lastMessage
        lastMessage = body

        return str(resp)
    return "yooooooo this is nothing"

if __name__ == "__main__":
    app.run('0.0.0.0')
