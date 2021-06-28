# from flask import render_template
# import connexion
import flask

# app = connexion.App(__name__, specification_dir='./')
app = flask.Flask(__name__)

# app.add_api('swagger.yml')


@app.route("/")
def home():
    # return render_template('home.html')
    return "Hello World!"


def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000, debug=True)
