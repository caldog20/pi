import I2C_LCD_driver as lcdrv
from time import *
lcd = lcdrv.lcd()
#name = raw_input("Type to display on screen: ")
#lcd.lcd_display_string_pos(name, 1, 5)
#sleep(1)
#lcd.lcd_clear()

def print_screen(string):
    lcd.lcd_display_string(string, 1)
    sleep(1)
    lcd.lcd_clear()



while True:
    string = raw_input("Type to print on screen: ")
    print_screen(string)
    sleep(1)
    lcd.lcd_clear
