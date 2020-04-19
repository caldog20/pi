import sys
sys.path.append('libs/')
import I2C_LCD_driver
import time
import Adafruit_DHT as dht
import pimods
import smbus

pcdaddr = 0x48
in0 = 0x40

bus = smbus.SMBus(1)
while True:
    bus.write_byte(address, in0)
    value = bus.read_byte(address)
    print(value)
    time.sleep(0.1)

