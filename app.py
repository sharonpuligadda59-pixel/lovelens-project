from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "replace-this-with-a-random-secret-before-deployment"

QUESTIONS = [
    {"id":"respect", "category":"Respect", "en":"Does your partner respect your opinions, even when they disagree?", "te":"Mee opinions tho agree kakapoyina, mee partner vaatini respect chesthaaraa?", "risk":False},
    {"id":"space", "category":"Boundaries", "en":"Can you spend time with friends or family without being punished or guilt-tripped?", "te":"Friends/family tho time spend chesthe mee partner mimmalni punish cheyyakunda, guilt feel cheyyinchakunda untaraa?", "risk":False},
    {"id":"support", "category":"Emotional support", "en":"Does your partner listen when you explain your feelings?", "te":"Meeru mee feelings cheppinappudu mee partner vintaraa?", "risk":False},
    {"id":"trust", "category":"Trust", "en":"Do you generally feel trusted without having to constantly prove where you are?", "te":"Meeru ekkada unnaro eppudu prove cheyyalsina pressure lekunda trust feel avuthaaraa?", "risk":False},
    {"id":"conflict", "category":"Communication", "en":"During disagreements, can both of you talk without insults or threats?", "te":"Arguments appudu insults leda threats lekunda maatladukogalara?", "risk":False},
    {"id":"control", "category":"Control", "en":"Does your partner repeatedly try to control what you wear, who you meet, or where you go?", "te":"Mee partner meeru em vesukovali, evarini kalavali, ekkadiki vellali ani repeated-ga control chesthaaraa?", "risk":True},
    {"id":"privacy", "category":"Privacy", "en":"Are you pressured to share passwords, private messages, or your live location?", "te":"Passwords, private messages, live location share cheyyamani pressure chesthaaraa?", "risk":True},
    {"id":"isolation", "category":"Isolation", "en":"Does your partner try to stop you from seeing friends or family?", "te":"Friends leda family ni kalavakunda mee partner aapadaniki try chesthaaraa?", "risk":True},
    {"id":"fear", "category":"Safety", "en":"Do you ever change what you say or do because you are afraid of your partner's reaction?", "te":"Mee partner reaction ki bhayapadi, meeru cheppe maatalu leda chese panulu marchukuntaaraa?", "risk":True},
    {"id":"humiliation", "category":"Respect", "en":"Does your partner repeatedly humiliate, threaten, or blame you to make you feel small?", "te":"Mee partner mimmalni repeated-ga avamaaninchadam, bedirinchadam, leda thakkuva-ga feel cheyyinchadam chesthaaraa?", "risk":True},
    {"id":"repair", "category":"Communication", "en":"After a disagreement, can your partner take responsibility and try to repair things?", "te":"Argument tarvatha mee partner tana thappu unte accept chesi situation improve cheyyadaniki try chesthaaraa?", "risk":False},
    {"id":"choice", "category":"Boundaries", "en":"Can you say “no” without being threatened, pressured, or punished?", "te":"Meeru “no” cheppinappudu threats, pressure, punishment lekunda untundaa?", "risk":True},
]
OPTIONS = [
    {"value":"often", "en":"Often", "te":"Chala saarlu"},
    {"value":"sometimes", "en":"Sometimes", "te":"Konni saarlu"},
    {"value":"rarely", "en":"Rarely", "te":"Chala takkuva"},
    {"value":"unsure", "en":"I'm not sure", "te":"Naaku clarity ledu"},
]

def lang():
    return session.get("lang", "en")

@app.context_processor
def inject_globals():
    return {"lang": lang(), "year": datetime.now().year}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/language", methods=["POST"])
def language():
    chosen = request.form.get("language", "en")
    session["lang"] = "te" if chosen == "te" else "en"
    return redirect(request.form.get("next") or url_for("home"))

@app.route("/check-in")
def check_in():
    return render_template("checkin.html", questions=QUESTIONS, options=OPTIONS)

@app.route("/results", methods=["POST"])
def results():
    answers = {q["id"]: request.form.get(q["id"], "unsure") for q in QUESTIONS}
    # Scoring is a simple reflection aid, not a validated psychological test.
    concern = 0
    positive = 0
    concern_items = []
    positive_items = []
    for q in QUESTIONS:
        answer = answers[q["id"]]
        if q["risk"]:
            if answer == "often":
                concern += 2
                concern_items.append(q)
            elif answer == "sometimes":
                concern += 1
                concern_items.append(q)
        else:
            if answer == "often":
                positive += 1
            elif answer == "rarely":
                concern += 1
                concern_items.append(q)
    if any(answers[k] == "often" for k in ["fear", "humiliation", "choice"]):
        level = "priority"
    elif concern >= 6:
        level = "high"
    elif concern >= 3:
        level = "moderate"
    else:
        level = "lower"
    session["last_result"] = {"level": level, "concern": concern, "positive": positive}
    return render_template("results.html", level=level, concern=concern, positive=positive,
                           concern_items=concern_items, positive_items=positive_items, questions=QUESTIONS)

@app.route("/advice")
def advice():
    return render_template("advice.html")

@app.route("/privacy", methods=["GET", "POST"])
def privacy():
    if request.method == "POST":
        session.pop("last_result", None)
        session.pop("lang", None)
        return redirect(url_for("privacy", cleared="1"))
    return render_template("privacy.html", cleared=request.args.get("cleared") == "1")

if __name__ == "__main__":
    app.run(debug=True)
