from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from get_ai_res import ask_ai
from xata.client import XataClient

# Xata API key and database URL
XATA_API_KEY = "YOUR_XATA_API_KEY"
XATA_DB_URL = "YOUR_XATA_DB_URL"

# Initialize XataClient with API key and database URL
xata = XataClient(api_key=XATA_API_KEY, db_url=XATA_DB_URL)

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent to our Twilio number
    body = request.values.get('Body', None)

    # Query data from Xata database
    data = xata.data().query("predictions", {
        "columns": [
            "label",
            "value"
        ]
    })

    # Call the ask_ai function to get the result
    result = ask_ai(data["records"], body)

    # Start our TwiML response
    if result:
        resp = MessagingResponse()
        resp.message(result)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
