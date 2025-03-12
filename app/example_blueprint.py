from flask import Blueprint, jsonify

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/user/<username>")
def get_user(username):
    if username.lower() == "jack":
        return jsonify({"message": "Valid User"}), 200
    else:
        return jsonify({"message": "Invalid User"}), 200