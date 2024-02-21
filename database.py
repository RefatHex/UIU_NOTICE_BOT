import firebase_admin
from firebase_admin import credentials, db
from firebase_admin import firestore
from TOKEN import DATABASE_URL

# Fetch the service account key JSON file contents
cred = credentials.Certificate('firebase-adminsdk.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': DATABASE_URL
})


class User:
    def __init__(self, user_id, username, name):
        self.user_id = user_id
        self.username = username
        self.name = name


def add_user_to_firestore(user):
    db_ref = db.reference('users').child(
        str(user.user_id))
    db_ref.set({
        'username': user.username,
        'name': user.name
    })


def read_users_from_firestore():
    users = []
    users_ref = db.reference('users').get()
    if users_ref is not None:
        for user_id, user_data in users_ref.items():  # Iterate through users
            users.append(
                User(user_id, user_data['username'], user_data['name']))
    return users


def is_user_in_firestore(user_id):
    user_ref = db.reference('users').child(
        str(user_id))
    user_data = user_ref.get()
    return user_data is not None  # Check if user exists
