from flask import Flask, render_template,request
app = Flask(__name__)

data = []

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
    global data
    data = request.get_json()
    print(data,calculateSpeed(data))
    return []

def calculateSpeed(data):
    return None

app.run(debug=True)