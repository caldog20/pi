import I2C_LCD_driver
from time import sleep
import wiringpi as wpi


wpi.wiringPiSetupGpio()
wpi.pinMode(21, 1)
mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()
wpi.digitalWrite(21,0)

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
        mylcd.lcd_display_string("Try Again, Invalid Input!", 1)
        sleep(0.5)
        wpi.digitalWrite(21,1)
        sleep(0.5)
        wpi.digitalWrite(21,0)
        sleep(0.5)
        wpi.digitalWrite(21,1)
        sleep(0.5)
        wpi.digitalWrite(21,0)
        mylcd.lcd_clear()


