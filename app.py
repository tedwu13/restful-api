from flask import Flask

app = Flask(__name__)

@app.route('/') #http://www.google.com/
def home():
    return "Hello World!"


app.run(port=5000) # run your app here with port 5000

#Google has many web servers
#Web server can have a response 
#What do we send to these web servers
#
#VERB/PROTOCOL/PATH WITH NEW HOST
#GET/HTTP/1.1
# GET /login HTTP/1.1
# Host: https://www.twitter.com


#POST /store data : {name:}
#GET /store/<string:name>
#GET /store
#POST /store/<string:name>/item {name:, price:}
#GET /store/<string:name>/item
