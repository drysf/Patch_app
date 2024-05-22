from app import app
from flask import request, render_template
from app.ShellCommand import ShellComands


@app.route('/Normalization', methods=["GET", "POST"])
def Normalization():
        nom_dossier = None
        if request.method == "POST":
            nom_dossier = request.form['nom_dossier']
            shell = ShellComands()
            shell.Normalization(inputFile=nom_dossier)
        return render_template("Normalization.html", nom_dossier=nom_dossier)

