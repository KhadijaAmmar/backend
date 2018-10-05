import flask
import shutil
import os
import random
# instantiate flask
app = flask.Flask(__name__)
app.url_map.strict_slashes = False



@app.route("/api/login", methods=['POST'])
def login():
    return ("ok")


# start the flask app, allow remote connections
app.run(host='0.0.0.0')
