import I2C_LCD_driver
import time

mylcd = I2C_LCD_driver.lcd()

str_pad = " " * 16

while True:
    mylcd.lcd_display_string_pos("Hey bitches!", 1, 0)
    time.sleep(1)
    str_pad = " " * 16
    my_long_string = "LOL"
    my_long_string = str_pad + my_long_string

    for i in range (0, len(my_long_string)):
        lcd_text = my_long_string[i:(i+16)]
        mylcd.lcd_display_string(lcd_text,1)
        time.sleep(0.09)
        mylcd.lcd_display_string(str_pad,1)
        
mylcd.lcd_display_string("Done!", 1)


