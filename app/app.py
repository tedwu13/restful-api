from flask import Flask, request
from flask_restful import Resource, Api,
from sqlalchemy import create_engine

from json import dumps

## Create an engine to connect to SQL lite 3 database
# In order to create a database in sqlite. run the command sqlite3 .mode csv db_name
# Then import the csv file into the database run the command .import employee.csv db_name
# 
# Start a virtual environment 
#

engine = create_engine('sqlite://salaries.db')

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
