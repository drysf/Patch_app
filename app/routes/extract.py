from app import app, render_template


@app.route('/Extract', methods=['GET', 'POST'])
def Extract():
    return render_template('Extract.html')
