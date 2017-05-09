# from werkzeug.security import safe_str_cmp # use safe string compare just to make sure and also all the encodings
# from user import User

# users = [
#     User(1, 'bob', 'asdf')
#     User(2, 'ted', 'lol')
#     User(3, 'teddy', 'lolteddy')
# ]

# username_mapping = { u.username: u for u in users }
# user_id_mapping = { u.id: u for u in users }

# # # two mapping dictionaries so that we can search by username or userid
# # username_mapping = {
# #     'bob': {
# #         'id': 1,
# #         'username': 'bob',
# #         'password': 'asdf'
# #     }
# # }


# # user_id_mapping = {
# #     1: {
# #         'id': 1,
# #         'username': 'bob',
# #         'password': 'asdf'
# #     }
# # }

# #dictionary.get(key)
# def authenticate(username, password):
#     #if user name is not in the username dictionary, return None
#     user = username_mapping.get(username, None)

#     if user and safe_str_cmp(user.password, password):
#         return user

# #identity function is a jwt thing
# def identity(payload):
#     user_id = payload['identity']
#     return user_id_mapping.get(user_id, None)


from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
