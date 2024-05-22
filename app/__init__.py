from flask import Flask, render_template, request


app = Flask(__name__)

from app.routes import route


app.run(debug=True)