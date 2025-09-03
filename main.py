
# ======================
# Imports
# ======================

from micropython import const
from lib.ili9341 import color565
from machine import idle, Pin, SPI
from init import display, touch, get_last_touch
import init
import time



# ======================
# NOTES
# ======================

# screen size ( in pixels )

#DISPLAY_WIDTH = 240
#DISPLAY_HEIGHT = 320

# display x cords ends at the left side, starts at right. Y cords are normal



# ======================
# Turn on the backlight
# ======================

BL_PIN = init.BL_PIN
Pin(BL_PIN, Pin.OUT).on()


# ======================
# Color Values
# ======================

BG_Color = color565(64, 64, 64)  # 64, 64, 64

Text_Color = color565(255, 255, 128) # 255, 255, 128 
Text_BG_Color = BG_Color # matches backgrounds

Menu_Text_Color = color565(255, 255, 128)

# ======================
# Button Ranges
# ======================
adjust_value = 10   # adjust this to move entire menu, higher makes it go lower

first_button_start = 51 + adjust_value
first_option_pos = first_button_start + 9
first_button_end   = 80 + adjust_value

second_button_start = 81 + adjust_value
second_option_pos = second_button_start + 9
second_button_end   = 110 + adjust_value

third_button_start  = 111 + adjust_value
third_option_pos = third_button_start + 9
third_button_end    = 140 + adjust_value

fourth_button_start = 141 + adjust_value
fourth_option_pos = fourth_button_start + 9
fourth_button_end   = 170 + adjust_value

fifth_button_start  = 171 + adjust_value
fifth_option_pos = fifth_button_start + 9
fifth_button_end    = 200 + adjust_value

# ======================
# Draw Menu
# ======================

print("Background")
display.clear(BG_Color)
time.sleep(1)

display.draw_text8x8(105, 20, "MENU", Menu_Text_Color, color565(64, 64, 64))


print("middle line")
display.draw_text8x8(115, 40, "|", color565(255, 255, 128), color565(64, 64, 64))

print("box / text")

# Box 1 - A
display.draw_line(0, first_button_start, 240, first_button_start, color565(255, 255, 255))
display.draw_text8x8(115, first_option_pos, "a", Text_Color, Text_BG_Color)
display.draw_line(0, first_button_end, 240, first_button_end, color565(255, 255, 255))
time.sleep(.1)

# Box 2 - B
display.draw_text8x8(115, second_option_pos, "b", Text_Color, Text_BG_Color)
display.draw_line(0, second_button_end, 240, second_button_end, color565(255, 255, 255))
time.sleep(.1)

# Box 3 - C
display.draw_text8x8(115, third_option_pos, "c", Text_Color, Text_BG_Color)
display.draw_line(0, third_button_end, 240, third_button_end, color565(255, 255, 255))
time.sleep(.1)

# Box 4 - D
display.draw_text8x8(115, fourth_option_pos, "d", Text_Color, Text_BG_Color)
display.draw_line(0, fourth_button_end, 240, fourth_button_end, color565(255, 255, 255))
time.sleep(.1)

# Box 5 - E
display.draw_text8x8(115, fifth_option_pos, "e", Text_Color, Text_BG_Color)
display.draw_line(0, fifth_button_end, 240, fifth_button_end, color565(255, 255, 255))


# ======================
# touch
# ======================

print("initiating touch")
try:
    while True:
        touch.get_touch()
        x, y = get_last_touch()
        
        if y is not None and first_button_start <= y <= first_button_end:  # Button A
            print("Touched > a")
            # Launch Next Script
            init.last_touch_x = None
            init.last_touch_y = None

        elif y is not None and second_button_start <= y <= second_button_end:  # Button B
            print("Touched > b")
            # Launch Next Script
            init.last_touch_x = None
            init.last_touch_y = None

        elif y is not None and third_button_start <= y <= third_button_end:  # Button C
            print("Touched > c")
            # Launch Next Script
            init.last_touch_x = None
            init.last_touch_y = None

        elif y is not None and fourth_button_start <= y <= fourth_button_end:  # Button D
            print("Touched > d")
            # Launch Next Script
            init.last_touch_x = None
            init.last_touch_y = None

        elif y is not None and fifth_button_start <= y <= fifth_button_end:  # Button E
            print("Touched > e")
            # Launch Next Script
            init.last_touch_x = None
            init.last_touch_y = None


except KeyboardInterrupt:
    print("\nCtrl-C pressed.  Cleaning up and exiting...")


#time.sleep(10)

#display.cleanup()
