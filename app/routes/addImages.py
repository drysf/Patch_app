from app import app, render_template


@app.route('/add_images', methods=["GET", "POST"])
def AddImages():
    return render_template("addImages.html")

