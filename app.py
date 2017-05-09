from flask import Flask, jsonify, request

app = Flask(__name__)


stores = [
    {
        'name': 'Apple Store',
        'items': [
            {
                'name': 'Computer Item',
                'price': 1510.99
            },
            {
                'name': 'Phone Item',
                'price': 200.11
            },
            {
                'name': 'Mouse',
                'price': 110.00
            }
        ]

    },
    {
        'name': 'Chipotle Store',
        'items': [
            {
                'name': 'Burrito',
                'price': 9.99
            },
            {
                'name': 'Bowl',
                'price': 11.00
            },
            {
                'name': 'Soft drink',
                'price': 3.99
            }

        ]

    }


]
@app.route('/') #http://www.google.com/
def home():
    return "Hello World!"


#POST /store data : {name:}
@app.route('/store', methods=['POST']) #http://localhost:5000/store/some_name
#some_name has to be the same as the argument
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    # iterate over stores
    # if the sotre name matches, return it
    # if none matches, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({ 'message': 'store not found' })


#GET /store
@app.route('/store')
def get_stores():
    return jsonify({ 'stores': stores})

#POST /store/<string:name>/item {name:, price:}

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({ 'message': 'store not found'})

#GET /store/<string:name>/item


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({ 'items': store['items']})
    return jsonify({ 'message': 'store not found'})


app.run(port=5000) # run your app here with port 5000
