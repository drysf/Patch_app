from app import app
from flask import request, render_template

@app.route("/upscale", methods=['GET', 'POST'])
def upscale():
    return render_template('upscaling.html')