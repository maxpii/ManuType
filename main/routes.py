from flask import render_template,request, flash, redirect, url_for
from main import app,db,bcrypt
from main.forms import RegistrationForm, LoginForm
from main.models import User, OneTest
from flask_login import login_user, current_user,logout_user, login_required


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
    if current_user.is_authenticated:
        return redirect(url_for("home_page"))
    form = RegistrationForm()
    if form.is_submitted() and form.validate() and form.validate_username(form.username) and form.validate_email(form.email):
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f"Account created for {form.username.data}! You can now login")
        return redirect(url_for("login_page"))
    
    elif form.is_submitted():
        if not form.validate_username(form.username):
            flash("username is taken")
        elif not form.validate_email(form.email):
            flash("email is taken")
        else:
            flash("Invalid data.")
    return render_template("register.html",form=form)

@app.route("/login", methods=["GET","POST"])
def login_page():
    form = LoginForm()
    if form.is_submitted() and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            flash("Login sucessful!")
            return redirect(url_for("home_page"))
    elif form.is_submitted() and not form.validate():
        flash("Login unsuccessful. Please check username and password")
        
    return render_template("login.html",form=form)

@app.route("/results")
def results_page():
    typing_data = OneTest(user_id=current_user.id, wpm=calculateSpeed(output), accuracy=calculateAccuracy(output))

    if current_user.is_authenticated:
        current_user.increment_total_tests()
        current_user.allTests.append(typing_data)
        db.session.commit()

    return render_template("results.html",data=[{"Speed": calculateSpeed(output), "Accuracy": calculateAccuracy(output)}])

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home_page"))

@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")



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
