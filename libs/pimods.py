#Custom Module for Functions and code
import time
import wiringpi as wpi
import I2C_LCD_driver as lcdctl
import Adafruit_DHT as dht

wpi.wiringPiSetupGpio()
wpi.pinMode(21, 1)



# Preset Variables for simplification
lcd = lcdctl.lcd()

# Print string on LCD - Simple
def lcdstring(string):
        lcd.lcd_clear()
        lcd.lcd_display_string(string, 1)
        time.sleep(1)
        lcd.lcd_clear()


# Blink RED LED function with custom iteration

def blinkred(red, numtimes):
    for i in range(0, numtimes):
        wpi.digitalWrite(red, 1)
        time.sleep(0.5)
        wpi.digitalWrite(red, 0)
        time.sleep(0.5)
        
# Blink Function for Scroll with for loop


def blinkscroll():
    wpi.digitalWrite(21, 1)
    time.sleep(0.09)
    wpi.digitalWrite(21, 0)
    time.sleep(0.09)



# Scroll Text Function with Blink
## Set stringscroll variable input as raw_input for string (python2 only)
def scroll_string(stringscroll):
    str_pad = " " * 16
    stringscroll = str_pad + stringscroll
    for i in range(0, len(stringscroll)):
        lcd_text = stringscroll[i:(i + 16)]
        lcdftn.lcd_display_string(lcd_text, 1)
        blinkscroll()
        lcdftn.lcd_display_string(str_pad, 1)


