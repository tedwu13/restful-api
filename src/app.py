from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)

app.secret_key = 'test_secret_key'
api = Api(app)
#Use Api to make things easier

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        # if the next function doesn't find anything return None
        return { 'item': item }, 200 if item else 404
    
    def post(self, name):
        #if content type is not application/json once force is set true
        #if silent is true, it returns None
        #request.get_json(force=True, silent=True)
        if next(filter(lambda x: x['name'] == name, items), None):
            return { 'message': "An item with name '{}' already exists.".format(name)}
        data = request.get_json()
        item = { 'name': name, 'price': data['price'] }
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return { 'items': items}

api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/item/itemName
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)

