from flask import Flask, render_template, request
import marks

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello():
    if request.method=="POST" or request.method=="GET":
        return render_template("index.html")

@app.route("/result", methods = ["POST"])
def fetch_exp():
    if request.method == "POST":
        name = request.form["name"]
        exp = request.form["exp"]
        if exp=="":
            string = "Atleast tell us your experience" 
        else:
            string = ""
        try:
            sal = marks.salary_prediction(float(exp))
        except:
            sal = 0
    return render_template("sub.html", sal = sal, name = name, string = string) 
   
if __name__ == "__main__":
    app.run(debug=True)