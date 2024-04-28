from flask import Flask, render_template,request
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "7c9a3daa9593e08a5cd46a6c85e2bdf2"
output = []

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/time")
def time_page():
    return render_template("time.html")

@app.route("/words")
def words_page():
    return render_template("words.html")

@app.route("/register")
def register_page():
    form = RegistrationForm()
    return render_template("register.html",form=form)

@app.route("/login")
def login_page():
    form = LoginForm()
    return render_template("login.html",form=form)

@app.route("/results")
def results_page():
    return render_template("results.html",data=[{"Speed": calculateSpeed(output), "Accuracy": calculateAccuracy(output)}])

@app.route("/process",methods=['POST'])
def process():
    global output
    output = request.get_json()
    print(output)
    return []

def calculateSpeed(data):
    return round(60/data["Time"] * data["Correct"]/5)

def calculateAccuracy(data):
    if data["Total"] == 0:
        return 0
    return round(data["Correct"]/data["Total"],2)

app.run(debug=True)