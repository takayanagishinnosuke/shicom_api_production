from flask import Flask, jsonify
from flask_cors import CORS
from requests import request
import os 
import face_recognition
import importlib


app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def test():
  # if request.method == 'GET':
    importlib.reload(face_recognition)
    keyval = face_recognition.key
    return keyval

if __name__ == "__main__":
    app.run(debug=True)

    