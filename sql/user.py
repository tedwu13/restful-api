import sqlite3
import flask_restful import Resource, reqparse
class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?" # parameter is a question mark (has to be a tuple)
        result = cursor.execute(query, (username, ))
        row = result.fetchone()

        if row:
            #user = cls(row[0], row[1], row[2])
            user = cls(*row)

        else:
            user = None

        connection.close()

        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?" # parameter is a question mark (has to be a tuple)
        result = cursor.execute(query, (_, ))
        row = result.fetchone()

        if row:
            #user = cls(row[0], row[1], row[2])
            user = cls(*row)

        else:
            user = None

        connection.close()

        return user



class UserRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("username",
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    parser.add_argument("password",
        type=str,
        required=True,
        help="This field cannot be blank"
    )

    def post(self):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        return { "message" : "User created successfully." }, 201
