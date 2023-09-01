from twilio.rest import Client

account_sid = 'ACb52443c00ba09c67eca74aa832b28d83'
auth_token = '4e1912a48c45409d8c427c414aee834d'
client = Client(account_sid, auth_token)

for i in range(10):
    message = client.messages.create(
        from_='+18886173743',
        body = "T madh",
        to='+38349101604'
    )

print(message.sid)