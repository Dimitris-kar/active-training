from flask import Flask, render_template, redirect
from datetime import datetime

today = datetime.now()
YEAR = today.strftime("%Y")

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html", year=YEAR)


if __name__ == "__main__":
    app.run(debug=True)

