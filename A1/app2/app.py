from flask import Flask, request, make_response
app = Flask(__name__)

import os
import hashlib
import json

## APP 2

@app.route('/')
def calculate_checksum():
    #Get JSON Object and check validity
    data = request.get_json()
    path = os.path.abspath('/app/data/' + data['file'])

    with open(path, "rb") as file:
        file_data = file.read()
        checksum = hashlib.md5(file_data).hexdigest()
        
    response = make_response(json.dumps(
        {
        "file": data['file'],
        "checksum": checksum
        }), 200)
        
    return response

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)
