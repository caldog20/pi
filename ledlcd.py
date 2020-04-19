import I2C_LCD_driver
from time import sleep
import wiringpi as wpi

str_pad = " " * 16
wpi.wiringPiSetupGpio()
wpi.pinMode(21, 1)
mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()
wpi.digitalWrite(21,0)

my_long_string = "Invalid Input, Try Again!"
my_long_stringg = "Enter 1 or 0 only!"
my_long_string = str_pad + my_long_string
my_long_stringg = str_pad + my_long_stringg

while True:
    try:
        var = int(input("Input: "))
    #var = int(testint)
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
        elif var > 1:
            print("GOOD")
            for i in range(0, len(my_long_stringg)):
                lcd_text = my_long_stringg[i:(i + 16)]
                mylcd.lcd_display_string(lcd_text, 1)
                blinkscroll()
                mylcd.lcd_display_string(str_pad, 1) 
    except NameError:
        print("Not an Integer")
        
    
        for i in range(0, len(my_long_string)):
            lcd_text = my_long_string[i:(i + 16)]
            mylcd.lcd_display_string(lcd_text, 1)
            blinkscroll()
            mylcd.lcd_display_string(str_pad, 1)
            


