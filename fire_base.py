
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
import get_message

def random_id():
    return random.randint(100000000, 999999999)
print("Running...")
while True:

    cred = credentials.Certificate("chatappdemo-6a01c-firebase-adminsdk-xnsij-b9101095da.json")
    firebase_admin.initialize_app(cred)


    db = firestore.client()


    messages_ref = db.collection('messages')

    docs = messages_ref.stream()



# sort by timestamp

    docs = messages_ref.order_by('timestamp').stream()
    for doc in docs:
        data = doc.to_dict()
        print(f"ID: {doc.id}")
        print(f"Received: {data['received']}")
        print(f"Text: {data['text']}")
        print(f"Timestamp: {data['timestamp']}")
    
# print message last update
    print(f"Last message: {data['text']}")    
# if the last message have received = True, then send message to firebase

    if data['received'] == True:
    # create a new message
        new_message = {
            'ID': random_id(),
            'received': False,
            'text': get_message.get_messge(data['text']),
        # 'timestamp': 2022-11-06 19:56:07.501430+00:00
            'timestamp': firestore.SERVER_TIMESTAMP
        }
        messages_ref.add(new_message)


print("Done")

