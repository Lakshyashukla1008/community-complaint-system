import hashlib
from database.database import users

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup_user(name, email, password):
    if users.find_one({"email": email}):
        return False

    users.insert_one({
        "name": name,
        "email": email.lower(),
        "password": hash_password(password)
    })

    return True


def login_user(email, password):
    user = users.find_one({
        "email": email,
        "password": hash_password(password)
    })

    return user