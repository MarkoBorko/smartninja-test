from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    name = "Marko"
    cities = ["Ljubljana", "Maribor", "Celje", "Vienna", "Rome"]
    #cities = None
    year = datetime.datetime.now().year
    return render_template("index.html", name=name, cities=cities, year=year)


@app.route("/about-me")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run()