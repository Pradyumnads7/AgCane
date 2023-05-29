from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def process_data():
    a = request.args.get('a')
    print("hello world")