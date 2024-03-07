from flask import Flask, render_template
app = Flask(__name__)

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

@app.route("/settings")
def settings_page():
    return render_template("settings.html")
    
app.run(debug=True)