from flask import Flask, render_template
import subprocess as sp

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/On")
def On():
    sp.call(["irsend", "SEND_ONCE", "Lights", "Key_Power"])
    print("Lights On / Off")
    return home()

@app.route("/BrightUp")
def BrightUp():
    sp.call(["irsend", "SEND_ONCE", "Lights", "Key_0"])
    print("Brighter")
    return home()

@app.route("/BrightDown")
def BrightDown():
    sp.call(["irsend", "SEND_ONCE", "Lights", "Key_1"])
    print("Dimer")
    return home()

@app.route("/White")
def White():
    sp.call(["irsend", "SEND_ONCE", "Lights", "Key_2"])
    print("White")
    return home()

@app.route("/Color")
def Color():
    sp.call(["irsend", "SEND_ONCE", "Lights", "Key_3"])
    print("Color")
    return home()

@app.route("/ChangeColor")
def ChangeColor():
    sp.call(["irsend", "SEND_ONCE", "Lights", "Key_4"])
    print("Change Color")
    return home()

@app.route("/Sunrise")
def Sunrise():
    sp.call(["irsend", "SEND_ONCE", "Lights", "Key_5"])
    print("Sunrise")
    return home()

if __name__ == "__main__":
    sp.call(["sudo", "/etc/init.d/lircd", "stop"])
    app.run(debug=True,  host='192.168.1.177', port=80 )
