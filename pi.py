from gpiozero import Motor, PWMOutputDevice
from flask import Flask, Response, request

ENA = PWMOutputDevice(12)
ENB = PWMOutputDevice(13)

ENA.value = 1.0
ENB.value = 1.0

motor_a = Motor(forward=26, backward=22)
motor_b = Motor(forward=27, backward=17)

app = Flask(_name_)

@app.route('/move', methods=['POST'])
def move():
    cmd = request.form.get('cmd')
    if cmd == 'w':
        motor_a.forward()
        motor_b.forward()
    elif cmd == 's':
        motor_a.backward()
        motor_b.backward()
    elif cmd == 'a':
        motor_a.forward()
        motor_b.backward()
    elif cmd == 'd':
        motor_a.backward()
        motor_b.forward()
    elif cmd == 'stop':
        motor_a.stop()
        motor_b.stop()
    return 'ok'

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)