# this file will be executed by the esp32 on boot. do not rename

from machine import I2C, Pin
import ssd1306
from time import sleep, ticks_ms
from uwebsockets import OP_PING, OP_PONG
# import uasyncio

i2c = I2C(scl=Pin(4), sda=Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 60)
button = Pin(25, Pin.IN, Pin.PULL_UP)

host = 'f1ff36994e3d.ngrok.io'
port = 80
ws = None

count = 0
last_state = 1

def do_wifi_connect():
    from network import WLAN, STA_IF
    wlan = WLAN(STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        render('connecting')
        wlan.connect('Bengtsons', '46322432')
        while not wlan.isconnected():
            pass
        render('connected')
    print('network config:', wlan.ifconfig())


def do_register(host, port):
    from uwebsockets import connect

    global ws
    if ws is None:
        ws = connect('ws://{}:{}/ws'.format(host, port))
        print('ws://{}:{}/ws'.format(host, port))
    render('register')
    ws.send('REGISTER')
    fin, opcode, data = ws.read_frame()
    resp = data.split(' ')
    assert resp[0] == 'REGISTERED'
    render('ID: {}'.format(resp[1]))

# async def handle_ping():
#     while True:
#         fin, opcode, data = await ws.read_frame()
#         if opcode == OP_PING:
#             ws.write_frame(OP_PONG, data)

def render(text):
    global oled
    oled.fill(0)
    oled.text("{}".format(text), 0, 0)
    oled.show()


do_wifi_connect()
do_register(host, port)
# handle_ping()

while True:
    button_state = button.value()

    if button_state == 0 and button_state != last_state:
        count += 1
        render(count)
        ws.send('SCORE {} {}'.format(ticks_ms(), count))

    last_state = button_state

    sleep(0.01)
