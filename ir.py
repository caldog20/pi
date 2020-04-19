import sys
sys.path.append('libs/')
import I2C_LCD_driver
import time
import Adafruit_DHT as dht
import pimods
import wiringpi as wpi
mylcd = I2C_LCD_driver.lcd()
wpi.piBoardRev()
wpi.wiringPiSetupGpio()
wpi.pinMode(21, 1)
wpi.pinMode(13, 0)
time.sleep(2)


while True:
    ir = wpi.digitalRead(13)
    if ir is 1:
        wpi.digitalWrite(21, 1)
        time.sleep(1)
    else:
        wpi.digitalWrite(21, 0)



