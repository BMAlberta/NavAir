from flask import Flask
from airports.service import airport_api

app = Flask(__name__)
app.register_blueprint(airport_api)

@app.route("/")
def home():
    return "Hello World!"


def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
