# RopeScore Clicker

TTGO esp32 OLED 18650 based hardware clicker for rope skipping

## Setup

Install micropython on the esp32 and transfer the files to it
see http://docs.micropython.org/en/latest/esp32/tutorial/intro.html#esp32-intro
and https://forums.4fips.com/viewtopic.php?f=3&t=6905 but tl;dr;

Download the latest stable micropython bin from
https://micropython.org/download/esp32/

```console
$ pip install -r requirements.txt
$ # not specifying a --port means it'll do it on whatever esp32 it can find
$ # it'll also snitch which port it uses for future reference
$ esptool.py erase_flash
$ esptool.py --chip esp32 write_flash -z 0x1000 esp32.bin
$ ampy --port COM3 put ssd1306.py
$ ampy --port COM3 put main.py
```
