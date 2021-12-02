from flask import Flask, render_template, json, request

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

#making page with info about candidate by chose id
@app.route("/candidate/<int:code>")
def candid_page(code):
     return render_template("candidate.html", candid=candidates, id=code)

#making page with candidate`s list
@app.route("/list/")
def list_page():
    return render_template("list.html", candid=candidates)

#making candidates names list
names_list = []
for i in candidates:
    names_list.append(i["name"])

print(settings["case-sensitive"])

#making page for searching candidates by their names or just by letters in names (also we will use or not the case-sensitivity which depends on set in settings)
@app.route("/search/")
def search_page():
    s = request.args.get("name")
    if s is None:
        return "Enter the name of candidate"
    if settings["case-sensitive"] == True:
        name_match = [name for name in names_list if s.lower() in name.lower()]
    else:
        name_match = [name for name in names_list if s in name]
        return name_match
    if len(name_match) == 0:
        return "No candidates in list with entered name. Try another one."
    else:
        return render_template("search.html", names=name_match, candid=candidates)



app.run()
