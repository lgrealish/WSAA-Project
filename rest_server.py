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
@app.route('/players/<string:name>', methods=['GET'])
def findbyname(name):
    return jsonify(playerDAO.findbyname(name))

# Create
@app.route('/players', methods=['POST'])
def create():
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
        return jsonify(newplayer)

# Update
@app.route('/players<string:name>', methods=['PUT'])
def update(name):
        jsonstring = request.json
        player={}
        if "Name" in jsonstring:
                player["Name"] = jsonstring["Name"]
        if "Club" in jsonstring:
                player["Club"] = jsonstring["Club"]
        if "Age" in jsonstring:
                player["Age"] = jsonstring["Age"]
        if "Position" in jsonstring:
                player["Position"] = jsonstring["Position"]
       
        updatedplayer = playerDAO.update(name, player)
        return jsonify(updatedplayer)
       
# Delete
@app.route('/players/<name>', methods=['DELETE'])
def delete(name):
        deletedplayer = playerDAO.delete(name)
        return jsonify(deletedplayer)
  
if __name__ == '__main__':
    app.run(debug=True)