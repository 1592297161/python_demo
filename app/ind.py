from flask import Flask, request, jsonify
from app import app
@app.route('/')
def hello_world():
    return 'Hello'