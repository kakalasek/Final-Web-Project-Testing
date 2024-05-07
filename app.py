from flask import Flask, request, jsonify, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/info")
def get_current_user():
    pass

@app.route('/register', methods=["POST"])
def register_user():
    pass

@app.route("/login", methods=["POST"])
def user_login():
    pass

@app.route("/logout", methods=["POST"])
def user_logout():
    pass

if __name__ == '__main__':
    app.run(debug=True, port=8080)