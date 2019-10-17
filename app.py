from flask import Flask, render_template
import subprocess as sp

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
@app.route("/On")
def On():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_POWER"])
    print("Lights On / Off")
    return home()
@app.route("/Bright")
def Bright():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_BRIGHTER"])
    print("Brighter")
    return home()
@app.route("/Dark")
def Dark():
    sp.call(["irsend", "SEND_ONCE", "dorm", "KEY_DARKER"])
    print("Darker")
    return home()
@app.route("/Red")
def Red():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_R"])
    print("Red")
    return home()
@app.route("/Green")
def Green():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_G"])
    print("Green")
    return home()
@app.route("/Blue")
def Blue():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_B"])
    print("Blue")
    return home()
@app.route("/White")
def White():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_W"])
    print("White")
    return home()
@app.route("/Orange")
def Orange():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_O"])
    print("Orange")
    return home()
@app.route("/Lgreen")
def Lgreen():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_LIME"])
    print("Light Green")
    return home()  
@app.route("/Lblue")
def Lblue():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_SKY"])
    print("Light Blue")
    return home()  
@app.route("/Ppink")
def Ppink():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_PALE_PINK"])
    print("Pale Pink")
    return home()  
@app.route("/Lorange")
def Lorange():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_O2"])
    print("Light Orange")
    return home()  
@app.route("/Pblue")
def Pblue():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_PALE_BLUE"])
    print("Pale Blue")
    return home()  
@app.route("/Purple")
def Purple():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_PURPLE"])
    print("Purple")
    return home()  
@app.route("/LLorange")
def LLorange():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_O3"])
    print("Lighter Orange")
    return home()  
@app.route("/SkyBlue")
def SkyBlue():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_MAIMI_BLUE"])
    print("Sky Blue")
    return home()  
@app.route("/Lpurple")
def Lpurple():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_PURPLE_2"])
    print("Light purple")
    return home()  
@app.route("/Yellow")
def Yellow():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_YELLOW"])
    print("Light Yellow")
    return home()  
@app.route("/AMarine")
def AMarine():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_AQUA_BLUE"])
    print("Aqua Marine")
    return home()  
@app.route("/HPink")
def HPink():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_HOT_PINK"])
    print("Hot Pink")
    return home()  
@app.route("/Jump7")
def Jump7():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_JUMP7"])
    print("Jump7")
    return home()  
@app.route("/Fade7")
def Fade7():
    sp.call(["irsend", "SEND_ONCE", "Dorm", "KEY_AUTO"])
    print("Fade")
    return home()  

if __name__ == "__main__":
    sp.call(["sudo", "/etc/init.d/lircd", "stop"])
    app.run(debug=True,  host='192.168.1.177', port=80 )
