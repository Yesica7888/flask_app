# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 09:20:32 2021

@author: Yésica
"""

"""from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

if __name__ == "__main__":
    app.run() """
    
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Probando funcionamiento local :D 1"

if __name__ == "__main__":
    app.run()