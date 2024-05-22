from app import app
from flask import request, render_template
from app.ShellCommand import ShellComands
from app.RundeckClass import Rundeck

@app.route('/', methods=["GET", "POST"])
def process():
        nom_dossier = None
        exportFile = None
        
        if request.method == "POST":
            
            nom_dossier = request.form['nom_dossier']
            exportFile = request.form['nom_export']
            shell = ShellComands()
            shell.Normalization(inputFile=nom_dossier)
            dateToday = ShellComands.GetDate()
            
            shell.AddImages(exportFile=exportFile , resultFile=f"result_{nom_dossier}_{dateToday}", inputFile=nom_dossier+"_nrm", outputFile=f"{nom_dossier}_patch_{dateToday}")
            
            shell.SendImagesInServer(inputFile=f"{nom_dossier}_patch_{dateToday}")
            
            Rundeck.EnvoiRundeck(patchName=f"{nom_dossier}_patch_{dateToday}", resultFile=f"result_{nom_dossier}_{dateToday}")
        return render_template("process.html", nom_dossier=nom_dossier, exportFile=exportFile)
