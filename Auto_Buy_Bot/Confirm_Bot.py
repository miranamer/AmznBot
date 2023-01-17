from twilio.rest import Client
import twilio_keys

def sendConfirmation():
    client = Client(twilio_keys.sid, twilio_keys.token)

    message = client.messages.create(
        body="Purchase Successful",
        from_=twilio_keys.twilio_number,
        to=twilio_keys.target_number
    )
