from flask import Flask, request
app = Flask(__name__)

import requests
import json
import os

## APP 1

@app.route('/checksum', methods=['POST', 'GET'])
def checksum():
    data = request.get_json()
    if 'file' not in data or not data['file']:
        return json.dumps(
            {
            "file": None,
            "error": "Invalid JSON input."
            }), 400
            
    # Check if file exists in mounted volume
    path = os.path.abspath('/app/data/' + data['file'])
    if not os.path.exists(path):
        return json.dumps(
            {
            "file": data['file'],
            "error": "File not found."
            }), 400
            
    # Send file to App 2 so that checksum can be calculated
    try:
        endpoint = 'http://app2:5001/'
        response = requests.get(endpoint, json=data)
    except requests.exceptions.RequestException as e:
        return 'Cannot reach checksum calculator'

    return response.text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
