from flask import Flask, render_template,request
app = Flask(__name__)
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

@app.route("/settings")
def settings_page():
    return render_template("settings.html")

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
    return (60/data["Time"] * data["Correct"]/5)

def calculateAccuracy(data):
    if data["Total"] == 0:
        return 0
    return (data["Correct"]/data["Total"])

app.run(debug=True)