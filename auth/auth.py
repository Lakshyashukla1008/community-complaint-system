import bcrypt
from database.database import users

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def signup_user(name, email, password):
    if users.find_one({"email": email.lower()}):
        return False    

    users.insert_one({
        "name": name,
        "email": email.lower(),
        "password": hash_password(password)
    })

    return True


def login_user(email, password):
    user = users.find_one({"email": email.lower()})

    if user and bcrypt.checkpw(
        password.encode(),
        user["password"]
    ):
        return user

    return None