from app import app
from flask import render_template, request
from .ShellCommand import ShellComands




#PROCESS 


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
        return render_template("process.html", nom_dossier=nom_dossier, exportFile=exportFile)








@app.route('/add_images', methods=["GET", "POST"])
def AddImages():
    return render_template("addImages.html")









@app.route('/Normalization', methods=["GET", "POST"])
def Normalization():
        nom_dossier = None
        if request.method == "POST":
            nom_dossier = request.form['nom_dossier']
            shell = ShellComands()
            shell.Normalization(inputFile=nom_dossier)
        return render_template("Normalization.html", nom_dossier=nom_dossier)







@app.route('/Extract', methods=['GET', 'POST'])
def Extract():
    return render_template('Extract.html')







@app.route('/Downloader', methods=['GET', 'POST'])
def Downloader():
    return render_template('Downloader.html')







if __name__ == '__main__':
    app.run(debug=True)
