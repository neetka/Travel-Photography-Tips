from flask import Flask, render_template, request, jsonify
import requests
import os


from flask_cors import CORS

app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app)

# API Configuration - REPLACE WITH YOUR ACTUAL API KEY
API_KEY = "QF5O3SBCg8-3hqf9ELXNWfhqZrdqKzlfDjhspGtDW-E"  # Change this!
API_ENDPOINT = "https://api.unsplash.com/search/photos"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    try:
        query = request.form.get("query", "")
    
        if not query:
            return jsonify({"error": "Empty query"}), 400
    
        params = {
            "query": query,
            "per_page": 9,
            "client_id": API_KEY
        }
    
    
        response = requests.get(API_ENDPOINT, params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API request failed: {str(e)}"}), 500
if __name__ == "__main__":
    app.run(debug=True, port=5001)