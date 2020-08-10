import time
from flask import Flask, jsonify
from multiprocessing import Process, Value
import datetime


app = Flask(__name__)


tasks = [
   {
      'id': 1,
      'title': u'Buy groceries',
      'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
      'done': False
   },
   {
      'id': 2,
      'title': u'Learn Python',
      'description': u'Need to find a good Python tutorial on the web', 
      'done': False
   }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
   return jsonify({'tasks': tasks})


x = 1
def record_loop(loop_on):
   while True:
      if loop_on.value == True:
         print(datetime.datetime.now())

      time.sleep(1)


if __name__ == "__main__":
   recording_on = Value('b', True)
   p = Process(target=record_loop, args=(recording_on,))
   p.start()  
   app.run(debug=True, use_reloader=False)
   p.join()

   # from gpiozero import LightSensor
   # ldr = LightSensor(21)

   # while True:
   #       print(ldr.value)

   # from gpiozero import MotionSensor
   #
   # pir = MotionSensor(20)
   #
   # while True:
   #    if pir.motion_detected:
   #    else:
   #       print("Nope")
