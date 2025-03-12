from flask import Blueprint

example_blueprint = Blueprint("example", __name__)

@example_blueprint.route("/")
def home():
    return "Hello CPS3500", 200  # Ensure this matches the expected output

@example_blueprint.route("/new_page")
def new_page():
    return "New Page Content", 200
@example_blueprint.route("/not_valid_user")
def not_valid_user():
    return "Invalid User", 200

@example_blueprint.route("/valid_user")
def valid_user():
    return "Valid User", 200
@example_blueprint.route("/example")
def example_route():
    return "Hello from Example Blueprint"


