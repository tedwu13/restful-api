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

e = create_engine('sqlite:///salaries.db')

app = Flask(__name__)
api = Api(app)

class Departments(Resource):
    def get(self):
        #Connect to database
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("SELECT DISTINCT DEPARTMENT from salaries")
        return {'departments': [i[0] for i in query.cursor.fetchall()]}
    
    def post(self):
        conn = e.connect()


class Positions(Resource):
    def get(self):
        #Connect to database
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("SELECT DISTINCT [Position Title] from salaries")
        return {'positions': [i[0] for i in query.cursor.fetchall()]}

class Names(Resource):
    def get(self):
        #Connect to a database
        conn = e.connect()
        query = conn.execute("SELECT DISTINCT Name from salaries")
        return {'names': [i[0] for i in query.cursor.fetchall()]}

class Salary(Resource):
    def get(self, department_name):
        conn = e.connect()
        department_name = department_name.upper()
        query = conn.execute("SELECT * from salaries where Department='%s'"%department_name)
        #Query the result and get cursor.
        #Dumping that data to a JSON is looked by extension

        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient

# class Employee(Resource):
#     def post(self):

#         parser = reqparse.RequestParser()

#         parser.add_argument('name', type=str, required=True, location='json')
#         parser.add_argument('department', type=str, required=True, location='json')
#         parser.add_argument('position', type=str, required=True, location='json')
#         parser.add_argument('salary', type=str, required=True, location='json')
        
#         args = parser.parse_args(strict=True) 

#         employee = {
#             'name': args['name'],
#             'department': args['department'],
#             'position': args['position'],
#             'salary': args['salary'],
#         }


 
api.add_resource(Salary, '/dept/<string:department_name>')
api.add_resource(Departments, '/departments')
api.add_resource(Names, '/names')
api.add_resource(Positions, '/positions')
if __name__ == '__main__':
     app.run()
