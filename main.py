from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Sefa Aydinelli </h1>"

@app.route("/whoami")
def who_am_i():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    return jsonify(firstname = firstname, lastname = lastname)

if __name__ == "__main__":
    app.run()