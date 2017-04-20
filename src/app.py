from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)
#Use Api to make things easier

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
    def post(self, name):
        item = { 'name': name, 'price': 12.00 }
        items.append(item)
        return item

api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/student/Rolf


app.run(port=5000)

