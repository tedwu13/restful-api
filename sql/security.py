from werkzeug.security import safe_str_cmp # for string comparision just to make sure all encodings are still the same
from user import User

def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


#identity function is a jwt thing

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id, None)
