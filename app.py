import requests
from flask import Flask, render_template

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=20").json()

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", pokemon=response["results"])


app.run(debug=True, port=8081)
