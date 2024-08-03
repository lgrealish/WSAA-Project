from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='',static_folder='staticpages')

# Set up initial home page and test
@app.route('/')
def index():
    return "Test"

if __name__ == '__main__':
    app.run(debug=True)