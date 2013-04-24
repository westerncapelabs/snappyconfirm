from flask import Flask, request, Response
from twilio.rest import TwilioRestClient
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Nothing to see!"


@app.route("/ticket/created", methods=['GET', 'POST'])
def ticket_created():
    # Twilio config
    account_sid = "XXXXXXXXXXXX"
    auth_token = "XXXXXXXXXXXX"
    to = "+1234567890"  # Any phone number you want to call
    from_ = "+1234567890"  # Must be a valid Twilio number

    # loads data from webhook and writes it to XML file
    data = json.loads(request.form["data"])
    ticket = data["ticket"]
    ticket_id = str(ticket["id"])
    summary = ticket["summary"]
    opener = ticket["opener"]["address"].split("@")
    name = opener[0]  # first part of email
    domain = opener[1]  # domain of the user

    xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response>"
    xml += "<Say>New Snappy ticket from " + name + " at " + domain + ". Message is "
    xml += summary + "</Say></Response>"

    f = open('ticket_' + ticket_id + '.xml', 'w')
    f.write(xml)
    f.close()

    # Initiates a twilio call
    client = TwilioRestClient(account_sid, auth_token)
    # Make the call
    url = "http://your-server-url/ticket/read/" + ticket_id
    call = client.calls.create(to=to,  # Any phone number
                               from_=from_,  # Must be a valid Twilio number
                               url=url)
    return call.sid, 200


@app.route("/ticket/read/<ticket_id>", methods=['GET', 'POST'])
def ticket_read(ticket_id):
    f = open('ticket_' + str(ticket_id) + '.xml', 'r')
    xml = f.read()
    return Response(xml, mimetype='text/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
