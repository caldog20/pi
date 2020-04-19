import sys
sys.path.append('libs/')
import I2C_LCD_driver
import time
import Adafruit_DHT as dht
import pimods
import smbus


bus = smbus.SMBus(1)
reading =- 1
while True:
    bus.write_byte(0x48, 0)
    value = bus.read_byte(0x48)
    print(value)
    time.sleep(1)

