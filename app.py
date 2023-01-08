from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/drone-service", methods = ["GET"])
def get_message_from_drone():
    return jsonify({"message": "hellow"})
if __name__ == "__main__":
    app.run(debug=True)
    

