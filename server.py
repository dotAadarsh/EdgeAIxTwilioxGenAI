from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

from xata.client import XataClient

XATA_API_KEY = "YOUR_XATA_DB_API"

XATA_DB_URL = "YOUR_XATA_DB_URL"


# Initialize XataClient with API key and database URL
xata = XataClient(api_key=XATA_API_KEY, db_url=XATA_DB_URL)

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    result = xata.data().ask("predictions", body)

    # Start our TwiML response
    resp = MessagingResponse()
    if result:
        resp.message(result["message"])

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
