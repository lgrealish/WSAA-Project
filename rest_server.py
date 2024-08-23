# rest_server.py
# Author: Linda Grealish
# This file contains all code for the creating FLASK server that links to a DAO

# import modules needed
from flask import Flask, url_for, request, redirect, abort, jsonify, render_template
from playerDAO import playerDAO

app = Flask(__name__, static_url_path='',static_folder='staticpages')

# Set up initial home page and test
@app.route('/')
def index():
    return render_template('playerdetails.html')


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
def create(id):
        # read json from the body
        jsonstring = request.json
        
        required_fields = ["Name", "Club", "Age", "Position"]
        for field in required_fields:
               if field not in jsonstring:
                abort(400, description=f"Missing required field: {field}")
                
               
        player = {
               "Name": jsonstring['Name'],
               "Club": jsonstring['Club'],
               "Age": jsonstring['Age'],
               "Position": jsonstring['Position']
        }
        newplayer = playerDAO.create(player)
        return jsonify(playerDAO.create(id))
'''
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
'''        
        #return jsonify(playerDAO.create(player))

# Update
@app.route('/players<name>', methods=['PUT'])
def update(name):
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
       
        return jsonify(playerDAO.update(name, player))
       
# Delete
@app.route('/players/<name>', methods=['DELETE'])
def delete(name):
        return jsonify(playerDAO.delete(name))
  
if __name__ == '__main__':
    app.run(debug=True)