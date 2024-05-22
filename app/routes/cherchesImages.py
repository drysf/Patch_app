from app import app, render_template


@app.route('/Cherche_les_images', methods=['GET', 'POST'])
def Cherche_les_images():
    return render_template('chercherDesImages.html')




