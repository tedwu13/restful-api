from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine

from json import dumps

## Create an engine to connect to SQL lite 3 database
# In order to create a database in sqlite. run the command sqlite3 .mode csv db_name
# Then import the csv file into the database run the command .import employee.csv db_name
# 
# Start a virtual environment 
# When you run app.py, you can curl the web address: curl http://127.0.0.1:5000 to get the data

engine = create_engine('sqlite://salaries.db')

app = Flask(__name__)
api = Api(app)

class Departments(Resource):
    def get(self):
        # Connect to database
        connect = engine.connect
        # Perform the query and return JSON data
        # query = connect.execute("SELECT ")


if __name__ == '__main__':
    app.run(debug=True)
