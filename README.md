# snappyconfirm

Python Flask-based app for phone driven notification and confirmation of Snappy helpdesk tickets. Uses Snappy webhooks (see [documentation](https://help.besnappy.com/webhooks)) to listen for a `ticket.created` event. Utilises a Twilio outbound phone call to read new ticket out to on-call staff member. Very simple hack, be gentle!

## Requirements

Python prereqs are maintained in `requirements.txt` but are roughly:

1. [Flask](http://flask.pocoo.org/docs/) (which relies on Werkzeug and Jinja2)
3. twilio-python

Other prereqs are:

1. Snappy account - [signup](http://www.besnappy.com/?utm_source=githum&utm_medium=web&utm_campaign=westerncapelabs) 
2. Twilio account - [signup](https://www.twilio.com/try-twilio)

## Environment Setup

Twilio has an awesome dev-environment setup guide for Flask and Twilio which we won't bother repeating. Just [read it](http://www.twilio.com/docs/quickstart/python/devenvironment) and follow along.

## Production Setup

You need something to run Flask app in for production. We recommend the nginx and uWSGI combo detailed [here](http://flask.pocoo.org/docs/deploying/uwsgi/).

## Config

Don't forget to update the Twilio account details and the server Twilio must callback to for its XML file.

## Run it!

	$ python snappyconfirm.py

Its now running on [http://yourserver:5000/ticket/created](http://yourserver:5000/ticket/created)

## Software is never done, just shipped.

This app is unsupported but pull-requests are always welcome. Enjoy!

## Snappy Data Structure Examples

### ticket.created 

    data = {u'ticket': {u'account_id': 1,
             u'created_at': 1366833953,
             u'created_via': u'email',
             u'default_subject': u'Hook test from email',
             u'first_staff_reply_at': None,
             u'id': 9999,
             u'last_reply_at': 1366833953,
             u'last_reply_by': u'customer',
             u'mailbox_id': 9999,
             u'next_recipients': u'{"cc":["Your Support &lt;support@example.com&gt;"],"bcc":[],"to":["Your Customer &lt;customer@example-customer.com&gt;"]}',
             u'opened_at': 1366833953,
             u'opened_by_contact_id': 2,
             u'opened_by_staff_id': None,
             u'opener': {u'account_id': 2,
                         u'address': u'customer@example-customer.com',
                         u'created_at': u'2012-12-10 14:47:51',
                         u'first_name': u'Your',
                         u'id': 37,
                         u'last_name': u'Custoemr',
                         u'provider': u'email',
                         u'updated_at': u'2012-12-10 14:47:51',
                         u'value': u'customer@example-customer.com'},
             u'status': u'waiting',
             u'summary': u'Just testing...\r   Mike',
             u'tags': [],
             u'updated_at': u'2013-04-24 20:05:53'}}