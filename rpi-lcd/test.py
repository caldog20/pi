import I2C_LCD_driver
import time
import Adafruit-DHT as dht
mylcd = I2C_LCD_driver.lcd()




# Temp/Humidity placeholder for function

sensor = 11
pin = 20
humidity, temperature = dht.read_retry(sensor, pin)
temperature = temperature * 9/5.0 + 32
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))

while True:
    mylcd.lcd_display_string_pos("Hey bitches!", 1, 0)

        
mylcd.lcd_display_string("Done!", 1)


