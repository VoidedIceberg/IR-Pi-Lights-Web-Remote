import subprocess as sp
import time
from contextlib import suppress

if __name__ == '__main__':
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
    time.sleep(3600)
    sp.Popen(["irsend", "SEND_ONCE", "Lights","POWER"])




