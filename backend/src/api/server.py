from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from operations import Operations
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

#Object for operations 
ops = Operations()



FLASK_PORT = int(os.getenv("FLASK_PORT", "5000"))
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "False").lower() == "true"

@app.route('/players', methods=["GET", "POST"]) 
def players_route():
    #Basic get all
    if request.method == "GET":
        status_code = 200
    #Post ing a player
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name")
        print("NAME IS:", name)
        ops.create(name)
        status_code = 201
    #Always return a updated list of player stats
    players = ops.update_stats()
    return jsonify(players), status_code

@app.route('/players/<id>', methods=["DELETE"]) 
def delete_player(id):
    ops.remove(id)
    players = ops.update_stats()
    return jsonify(players), 204




if __name__ == '__main__':
    app.run(debug=FLASK_DEBUG, port=FLASK_PORT)
