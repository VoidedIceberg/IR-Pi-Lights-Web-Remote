import datetime
import time

from suntime import Sun, SunTimeException
import subprocess as sp

latitude = 46.758801
longitude = -96.903809
sun = Sun(latitude, longitude)

def init():
    sp.call(["sudo", "/etc/init.d/lircd", "stop"])
    print("Init ran")

def main():
    print("Main Running")
    today_sr = getTodayTime();
    # sunriseSequence()
    while True:
        time.sleep(25)
        date = datetime.datetime.now()
        print("--------------------------")
        print(date.hour + date.minute)
        print(today_sr.time().hour + today_sr.time().minute)

        if (date.hour + date.minute) == 82:
                print("It's a new dawn....its a new day....and I'm feeling good")
                today_sr = getTodayTime()
        if (date.hour == today_sr.time().hour) and (date.minute == today_sr.time().minute):
            print("The sun will rise!")
            sunriseSequence()

def sunriseSequence():
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "POWER"])  # turns lights on
    time.sleep(1)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "COLOR"])  # Switch to color mode
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights","DIMMER"])
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights","DIMMER"])
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights","DIMMER"])
    time.sleep(300)

    sp.Popen(["irsend", "SEND_ONCE", "Lights", "COLOR"])  # Switch to color mode
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights","BRIGHTER"])
    time.sleep(0.5)

    time.sleep(300)

    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights","BRIGHTER"])
    time.sleep(0.5)

    time.sleep(300)

    sp.Popen(["irsend", "SEND_ONCE", "Lights", "COLOR"])  # Switch to color mode
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)

    time.sleep(300)

    sp.Popen(["irsend", "SEND_ONCE", "Lights", "COLOR"])  # Switch to color mode
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights", "SWITCH_COLOR"]) #Switch to Red
    time.sleep(0.5)
    sp.Popen(["irsend", "SEND_ONCE", "Lights","BRIGHTER"])

    time.sleep(300)

    sp.Popen(["irsend", "SEND_ONCE", "Lights","WHITE"])



def getTodayTime():
    # Get today's sunrise and sunset in UTC
    today_sr = sun.get_sunrise_time()
    today_ss = sun.get_sunset_time()
    print('Today at Worcester the sun raised at {} and get down at {} UTC'.
          format(today_sr.strftime('%H:%M'), today_ss.strftime('%H:%M')))
    return today_sr

if __name__ == "__main__":
    init()
    main()