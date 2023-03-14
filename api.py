from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import json

from generator import main

import logging

# Configure the logger to write to a file
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('myapp.log')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)
CORS(app)
path = '/path/to/upload/folder'

ALLOWED_EXTENSIONS = set(['json', 'xlxs'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])


app = Flask(__name__)

@app.route("/api", methods=["POST"])
def receive_json():
    data = request.get_json()
    logger.info('Received data: %s', data)
    name = data["course_name"]
    # Process the received JSON data here...
    filename = name +".json"
    with open(filename, "w") as file:
        json.dump(data, file)

    main(filename)
    os.remove(filename)

    print("Received data:", data)

    
    return jsonify({"success": True})


@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    else:
        return jsonify({'error': 'File not found'})


app.config['UPLOAD_FOLDER'] = path
app.run()
