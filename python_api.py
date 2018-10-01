import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>This is our api</h1>'''

@app.route('/api/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('test.db')
    all_records = conn.execute("SELECT * FROM COMPANY;").fetchall()
    return jsonify(all_records)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 This is not the page you are looking for</h1>", 404

app.run()