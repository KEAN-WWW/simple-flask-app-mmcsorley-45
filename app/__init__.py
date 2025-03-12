from flask import Flask

from app.example_blueprint import user_blueprint
from app.example_module import example_blueprint


app = Flask(__name__)
app.register_blueprint(example_blueprint)
app.register_blueprint(user_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
