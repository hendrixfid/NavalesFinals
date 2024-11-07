import requests
import json
from faker import Faker
from webexteamssdk import WebexTeamsAPI


accessToken = "ODM2ZDA0ZTUtNzdlNS00NWIxLThiZDAtNGJiYmI0YzY5ZDQ5YmQzNDMzOTUtN2Ew_P0A1_bc884c7a-820b-497b-8b60-00b4d15ea95d"
api = WebexTeamsAPI(access_token= accessToken)

#PART 1

#Question 1
inputRoom = input("Please enter a room name: ")

room = api.rooms.create(inputRoom)
print(f'Room created with ID: {room.id}')
print()

inputMessage = input("Please enter your message: ")
message = api.messages.create(room.id, text=inputMessage)
print('Message sent!')

#Question 2
email_list = ['ellisnuevas00@gmail.com','keanandreimatic@baliuagu.edu.ph', 'igaya82@gmail.com','jacobpalenciaau@gmail.com','aaronalejandro308@gmail.com']

def userAddToRoom(room_id, email_list):
    for email in email_list:
        try:
            api.memberships.create(roomId=room_id, personEmail=email)
            print(f'Added {email} to the room.')
        except Exception as e:
            print(f'Failed to add {email} to the room: {str(e)}')

userAddToRoom(room.id, email_list)


#Question 3
def list_room_messages(room_id):
    messages = api.messages.list(roomId=room_id)
    for message in messages:
        print(f'Message ID: {message.id}, Text: {message.text}')

def deleteMessage(message_id):
    try:
        api.messages.delete(message_id)
        print(f'Message with ID {message_id} deleted.')
    except Exception as e:
        print(f'Failed to delete message with ID {message_id}: {str(e)}')

print('Listing all messages in the room:')
list_room_messages(room.id)

inputMessageId = input("Please enter the message ID to delete: ")
deleteMessage(inputMessageId)






#PART 2

fake = Faker()


userProfiles = []
for _ in range(10):
    profile = {
        'Full name': fake.name(),
        'Email address': fake.email(),
        'Job title': fake.job(),
        'Company': fake.company()
    }
    userProfiles.append(profile)

    print(f"Full Name: {profile['Full name']}, Email Address: {profile['Email address']}, Job Title: {profile['Job title']}, Company: {profile['Company']}")



import random
import string 

for _ in range(10):
    transac_ID = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    transac_date = fake.date(pattern="%Y-%m-%d")
    amount = round(random.uniform(100.00, 5000.00), 2)
    print(f"Transaction ID: {transac_ID}, Transaction date: {transac_date}, Amount: {amount}")
