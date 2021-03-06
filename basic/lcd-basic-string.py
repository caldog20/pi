import I2C_LCD_driver
from time import sleep
import wiringpi as wpi
import sys
sys.path.append('libs/')

str_pad = " " * 16
wpi.wiringPiSetupGpio()
wpi.pinMode(21, 1)
mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()
wpi.digitalWrite(21,0)

my_long_string = "Invalid Input, Try Again!"
my_long_string = str_pad + my_long_string

while True:
    var = int(input("Input:"))
    if var is 1:
        wpi.digitalWrite(21,1)
        mylcd.lcd_display_string("LED IS ON", 1)
        sleep(2)
        mylcd.lcd_clear()
    elif var is 0:
        wpi.digitalWrite(21,0)
        mylcd.lcd_display_string("LED IS OFF", 1)
        sleep(2)
        mylcd.lcd_clear()
    else:
        for i in range(0, len(my_long_string)):
            wpi.digitalWrite(21,1)
            sleep(0.5)
            wpi.digitalWrite(21,0)
            lcd_text = my_long_string[i:(i + 16)]
            mylcd.lcd_display_string(lcd_text, 1)
            sleep(0.09)
            mylcd.lcd_display_string(str_pad, 1)
