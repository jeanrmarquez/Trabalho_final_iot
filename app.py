from flask import Flask, render_template
import RPi.GPIO as GPIO
from random import randint
import time
import serial

comunicacaoSerial = serial.Serial('/dev/ttyUSB0', 9600)

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
rele = 16
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

    comunicacaoSerial.flush()
    comunicacaoSerial.flushInput()
    comunicacaoSerial.flushOutput()
    time.sleep(2)

    dados = comunicacaoSerial.readline()
    string_a_tratar = str(dados)

    temp_and_hum = string_a_tratar.split("e")
    umidade = temp_and_hum[0].split("b'")
    temperatura = temp_and_hum[1].split("\\r")

    umidade_float = float(umidade[1])
    temperatura_float = float(temperatura[0])

    humidity = '{0:0.1f}'.format(umidade_float)
    temperature = '{0:0.1f}'.format(temperatura_float)
    print(humidity)
    print(temperature)

    templateData = {
        'temperature': temperature,
        'humidity': humidity
    }

    return render_template('index.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)