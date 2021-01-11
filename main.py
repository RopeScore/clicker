# this file will be executed by the esp32 on boot. do not rename

import machine, ssd1306
from time import sleep

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 60)
button = machine.Pin(25, machine.Pin.IN, machine.Pin.PULL_UP)

count = 0
last_state = 1


def render (count):
    global oled
    oled.fill(0)
    oled.text("{}".format(count), 0, 0)
    oled.show()

render(count)

while True:
    button_state = button.value()

    if button_state == 0 and button_state != last_state:
        count += 1
        render(count)

    last_state = button_state

    sleep(0.01)
