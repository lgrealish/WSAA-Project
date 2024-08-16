# rest_server.py
# Author: Linda Grealish
# This file contains all code for the creating FLASK server that links to a DAO

# import modules needed
from flask import Flask, url_for, request, redirect, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from playerDAO import playerDAO

app = Flask(__name__, static_url_path='',static_folder='staticpages')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up initial home page and test
@app.route('/')
def index():
    return "Test"

# Get All
@app.route('/players', methods=['GET'])
def getAll():
    return jsonify(playerDAO.getAll())

# Find by Name
@app.route('/players/<name>', methods=['GET'])
def findbyname(name):
    return jsonify(playerDAO.findbyname(name))

# Create
@app.route('/players', methods=['POST'])
def create():
        # read json from the body
        jsonstring = request.json
        player = {}

        if "name" not in jsonstring:
                abort(402)
        player["name"] = jsonstring["name"]
        if "club" not in jsonstring:
                abort(402)
        player["club"] = jsonstring["club"]
        if "age" not in jsonstring:
                abort(402)
        player["age"] = jsonstring["age"]
        if "position" not in jsonstring:
                abort(402)
        player["position"] = jsonstring["position"]
        
        return jsonify(playerDAO.create(player))

# Update
@app.route('/players', methods=['PUT'])
def update():
        jsonstring = request.json
        player={}
        if "name" in jsonstring:
                player["name"] = jsonstring["name"]
        if "club" in jsonstring:
                player["club"] = jsonstring["club"]
        if "age" in jsonstring:
                player["age"] = jsonstring["age"]
        if "position" in jsonstring:
                player["position"] = jsonstring["position"]
    
        return jsonify(playerDAO.update(id, player))
       

  
if __name__ == '__main__':
    app.run(debug=True)