import csv
import os


class User:
    def __init__(self, user_id, username, name):
        self.user_id = user_id
        self.username = username
        self.name = name

def add_user_to_csv(user):
    file_exists = os.path.isfile('users.csv')
    with open('users.csv', 'a', newline='') as csvfile:
        fieldnames = ['user_id', 'username', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'user_id': user.user_id, 'username': user.username, 'name': user.name})


def read_users_from_csv():
    users = []
    with open('users.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(User(int(row['user_id']), row['username']))
    return users

def is_user_in_csv(user_id):
    with open('users.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['user_id']) == user_id:
                return True
    return False
