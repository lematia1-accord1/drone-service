# import the required packages
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# init app
app = Flask(__name__)
# create a route for drone_service
@app.route("/drone-service", methods = ["GET"])
def get_message_from_drone():
    return jsonify({"message": "hellow"})
# run the server
if __name__ == "__main__":
    app.run(debug=True)