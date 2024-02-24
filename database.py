import firebase_admin
from firebase_admin import credentials, db
from TOKEN import DATABASE_URL

# Fetch the service account key JSON file contents
cred = credentials.Certificate('firebase-adminsdk.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': DATABASE_URL
})


class User:
    def __init__(self, user_id, username=None, name=None):
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


def read_users_from_db():
    users = []
    users_ref = db.reference('users').get()
    if users_ref is not None:
        for user_id in users_ref.keys():  # Iterate through user IDs
            users.append(User(user_id))
    return users


def is_user_in_firestore(user_id):
    user_ref = db.reference('users').child(
        str(user_id))
    user_data = user_ref.get()
    return user_data is not None


def add_notice_to_db(notice_text):
    db.reference('notices').push().set({'text': notice_text})


def get_last_notice_from_firestore():
    last_notice_ref = db.reference(
        'notices').order_by_key().limit_to_last(1).get()
    if last_notice_ref:
        last_notice_key, last_notice_data = last_notice_ref.popitem()
        return last_notice_data.get('text')
    return None
