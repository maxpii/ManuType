from flask import Flask, render_template,request, flash, redirect, url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "7c9a3daa9593e08a5cd46a6c85e2bdf2"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False) #string of 20 characters, and cannot be duplicated
    email = db.Column(db.String(120), unique=True, nullable=False) #string of 20 characters, and cannot be duplicated
    image_file = db.Column(db.String(20),nullable=False, default='default.jpg') #string of 20 characters, and cannot be duplicated
    password = db.Column(db.String(60), nullable=False)
    #TODO:create columns for typing-specific data

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

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

@app.route("/register", methods=["GET","POST"])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!")
        return redirect(url_for("home_page"))
    elif form.is_submitted() and not form.validate():
        flash("Invalid data")
    return render_template("register.html",form=form)

@app.route("/login", methods=["GET","POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in")
            return redirect(url_for("home_page"))
    elif form.is_submitted() and not form.validate():
        flash("Login unsuccessful. Please check username and password")
    return render_template("login.html",form=form)

@app.route("/results")
def results_page():
    return render_template("results.html",data=[{"Speed": calculateSpeed(output), "Accuracy": calculateAccuracy(output)}])

@app.route("/process",methods=['POST'])
def process():
    global output
    output = request.get_json()
    return []

def calculateSpeed(data):
    return round(60/data["Time"] * data["Correct"]/5)

def calculateAccuracy(data):
    if data["Total"] == 0:
        return 0
    return round(data["Correct"]/data["Total"],2)

app.run(debug=True)