from flask import Flask, render_template
import RPi.GPIO as GPIO
from random import randint
 
app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
rele = 16
sensor = 23

GPIO.setup(rele, GPIO.OUT)

GPIO.output(rele, GPIO.HIGH)

@app.route("/") 
def main():
   return render_template('index.html')
 
@app.route("/<pin>/<action>")
def sensor(pin, action):
   temperature = ''
   humidity = ''

   if pin == "rele" and action == "on":
      GPIO.output(rele, GPIO.LOW)
      print('on')
   if pin == "rele" and action == "off":
      GPIO.output(rele, GPIO.HIGH)
      print('off')
    

   temperature = randint(0, 100) 
   humidity =  randint(0, 100)
 
   templateData = {
   'temperature' : temperature,
   'humidity' : humidity
   }
 
   return render_template('index.html', **templateData)



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
