from flask import Flask, request, jsonify
import json

app = Flask(__name__)
client = app.test_client()

tutorials = [
    {
        "title": "Video #1. Intro",
        "description": "GET, POST routes"
    },
    {
        "title": "Video #2. More features",
        "description": "GET, POST routes"
    }
]

@app.get('/tutorials')
def get_list():
    return jsonify(tutorials)

@app.post('/tutorials')
def update_list():
    new_one = request.json
    tutorials.append(new_one)
    return jsonify(tutorials)