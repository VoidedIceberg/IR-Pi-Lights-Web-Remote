from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/On")
def On():
    print("Lights On / Off")
    return home()

@app.route("/BrightUp")
def BrightUp():
    print("Brighter")
    return home()

@app.route("/BrightDown")
def BrightDown():
    print("Dimer")
    return home()

@app.route("/White")
def White():
    print("White")
    return home()

@app.route("/Color")
def Color():
    print("Color")
    return home()

@app.route("/ChangeColor")
def ChangeColor():
    print("Change Color")
    return home()

@app.route("/Sunrise")
def Sunrise():
    print("Sunrise")
    return home()

if __name__ == "__main__":
    app.run(debug=True)