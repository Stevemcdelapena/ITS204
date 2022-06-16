from twilio.rest import Client
import datetime

# Your Account SID from twilio.com/console
account_sid = "AC2955fc69afa62e1c201ad78006e820ca"
# Your Auth Token from twilio.com/console
auth_token  = "13c1e18b561c1976bd92726dd7fe5ea9"

client = Client(account_sid, auth_token)

userName = str(input("Enter your Fullname (Firstname Middlename Lastname):\n"))
birthYear = int(input("Enter year birthdate(yyyy): "))
birthMonth = int(input("Enter month birthdate(mm): "))
birthDay = int(input("Enter your birthdate(dd): "))

age = datetime.datetime.now().year - birthYear
sAge = str(age)

x = "Happy" + sAge + "Birthday!, " + userName

message = client.messages.create(
    to="+639380885566", 
    from_="+19807058368",
    body=x)

print(message.sid)
