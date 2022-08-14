from flask import Flask, render_template

from random import randint
 
app = Flask(__name__)

state = False

@app.route("/") 
def main():
   return render_template('index.html')
 
@app.route("/<pin>/<action>")
def sensor(pin, action):
   global state
   temperature = ''
   humidity = ''

   if pin == "rele" and action == "on":
      state = True
      print("Pin 1 is on")
   if pin == "rele" and action == "off":
      state = False
      print("Pin 1 is off")


   temperature = randint(0, 100) 
   humidity =  randint(0, 100)
 
   templateData = {
   'temperature' : temperature,
   'humidity' : humidity
   }
 
   return render_template('index.html', **templateData)


@app.route("/rele", methods=['GET'])
def rele():
   global state
   if state == False:
      state = True
      print("Ligado")
   else:
      state = False
      print("Desligado")
   return True

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)