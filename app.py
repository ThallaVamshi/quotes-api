from flask import Flask, jsonify
from scraper import get_quotes

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Quotes API is running"}

@app.route("/quotes")
def quotes():
    return jsonify(get_quotes())

if __name__ == "__main__":
    app.run(debug=True, port=5000)

