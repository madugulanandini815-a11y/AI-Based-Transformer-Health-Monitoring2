from flask import Flask, request, jsonify

app = Flask(__name__)

latest_data = {}

@app.route('/data', methods=['POST'])
def receive_data():
    global latest_data
    latest_data = request.json
    print("Received:", latest_data)
    return jsonify({"status": "received"})

@app.route('/get', methods=['GET'])
def get_data():
    return jsonify(latest_data)

app.run(host="0.0.0.0", port=5000)
