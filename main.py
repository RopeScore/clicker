# this file will be executed by the esp32 on boot. do not rename

import machine, ssd1306

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 60)

oled.fill(0)
oled.text("Hello World!", 0, 0)
oled.show()
