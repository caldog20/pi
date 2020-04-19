import sys
sys.path.append('libs/')
import I2C_LCD_driver
import time
import Adafruit_DHT as dht
import pimods


while True:
    #mylcd.lcd_clear()
    #mylcd.lcd_display_string("Reading DHT11", 1)
    humidity, temperature = dht.read_retry(11, 20)
    temperature = temperature * 9/5.0 + 32
    mylcd.lcd_clear()
    if humidity is not None and temperature is not None:
        temp = 'Temp={0:0.1f}*'.format(temperature)
        humid = 'Humidity={0:0.1f}%'.format(humidity)
        mylcd.lcd_display_string_pos(temp, 1, 0)
        mylcd.lcd_display_string_pos(humid, 2, 0)
        
        if temp > 50:
            pimods.blinkred(21, 3)
        


