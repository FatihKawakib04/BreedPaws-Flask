from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/gallery.html")
def gallery():
    return render_template('gallery.html')

@app.route("/services.html")
def services():
    return render_template('services.html')

@app.route("/team.html")
def team():
    return render_template('team.html')

@app.route("/404.html")
def error_page():
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True)
