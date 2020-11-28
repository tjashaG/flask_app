from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/HairdresserHans")
def hairdresser_hans():
    return render_template("hairdresser_hans_index.html")

@app.route("/Fakebook")
def fakebook():
    return render_template("Fakebook_index.html")


if __name__ == "__main__":
    app.run()
