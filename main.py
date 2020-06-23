from flask import Flask, render_template
import random
import AutoWhats
app = Flask(__name__)
from threading import *


@app.route("/")
def hello():
    AutoWhats.getqr()
    return render_template('index.html',rval=random.randint(11111,22222))

class service(Thread):
  def run(self):
    AutoWhats.start()

s1 = service()


@app.route("/start")
def serve():
    s1.start()
    return 'service started.<br><br>To Stop Click <a href="./stop">here</a>'

@app.route("/stop")
def stp():
    exit()
    return 'service ended'

@app.route("/dummy")
def dummy():
    return 'dummy called'

@app.route("/resume")
def resume():
    AutoWhats.resume()
    return 'service resumed'