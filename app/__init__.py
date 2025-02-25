from flask import Flask

#initialixe Flask service
app = Flask(__name__)
app.register_blueprint(example_blueprint)