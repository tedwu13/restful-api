from werkzeug.security import safe_str_cmp # for string comparision just to make sure all encodings are still the same
from user import User

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
    User(3, 'user3', '123'),
]


#two mapping dictionaries so that we can search by username or userid
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


#identity function is a jwt thing

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
