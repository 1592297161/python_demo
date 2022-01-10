from flask import Flask, request, jsonify
from app import app
@app.route('/w')
def hello_world11():
    return 'Hell111111111o'