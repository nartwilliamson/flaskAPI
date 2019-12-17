from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name':'My Item',
                'price': 15.99
            }
        ]
    }
]


# from the server perspective
# Post - used to receive data from client
# Get - used to send data back to client



#Post /store data: {name:}
@app.route('/store' , methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#Get /store/<string:name>
@app.route('/store/<string:name>') #http://127.0.0.1:5000/store/some_name
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})
    #iterate over stores, if the store name matches return store
    # if none match return error


#Get /store
@app.route('/store') 
def get_stores():
    return jsonify({'stores':stores})

#Post /store/<string:name/item
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
    pass

#Get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000)

