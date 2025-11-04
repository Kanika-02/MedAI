from flask import Flask, render_template, request, jsonify
from model import get_diagnosis

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_diagnosis(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
