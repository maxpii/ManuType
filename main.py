from flask import Flask, render_template,request
app = Flask(__name__)

wordData = []

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

@app.route("/process",methods=['POST'])
def process():
    data = request.get_json()
    wordData = data
    print(wordData)
    return []



app.run(debug=True)