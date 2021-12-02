from flask import Flask, render_template, json

#loading data from candidates.json
with open("candidates.json", "r", encoding="UTF-8") as file:
    candidates = json.load(file)

#loading data from settings.json
with open("settings.json", "r") as file:
    settings = json.load(file)

app = Flask(__name__)

#making root page, and showing status "online" from settings.json file
@app.route("/")
def main_page():
    return render_template("main.html", set=settings)

# @app.route("/")
# def main_page():
#     return render_template("main.html", set=settings)

app.run()