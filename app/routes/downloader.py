from app import app, render_template


@app.route('/Downloader', methods=['GET', 'POST'])
def Downloader():
    return render_template('Downloader.html')

