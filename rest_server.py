from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='',static_folder='staticpages')

# Set up initial home page and test
@app.route('/')
def index():
    return "Test"

# Get All
@app.route('/players', methods=['GET'])
def getAll():
    return jsonify(players)

# Find by Name
@app.route('/players/<int:id>', methods=['GET'])
def findbyid():
    return jsonify(players)

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