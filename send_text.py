from twilio.rest import TwilioRestClient

account_sid = "AC1aa4bc1b52de2ff98ed526b8809f5faf" # Your Account SID from www.twilio.com/console
auth_token  = "acd5014479cc9e3b8a3e1dc034adc772"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python",
    to="+919003715607",    # Replace with your phone number
    from_="+12569800360") # Replace with your Twilio number

print(message.sid)
