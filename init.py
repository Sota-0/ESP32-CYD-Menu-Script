from micropython import const
from lib.ili9341 import Display, color565
from lib.xpt2046 import Touch
from machine import idle, Pin, SPI


# to use: refer to cheat sheet for more info


# ==========================
# Display configuration
# ==========================

DISPLAY_WIDTH = const(240)
DISPLAY_HEIGHT = const(320)
ROTATION = const(180)  # Matches your working example - original 270 or Rotation must be 0, 90, 180 ( right way up) or 270.


SPI1_BAUD_RATE = const(40000000)
SPI1_SCK_PIN = const(14)
SPI1_MOSI_PIN = const(13)
DISPLAY_DC_PIN = const(2)
DISPLAY_CS_PIN = const(15)
DISPLAY_RST_PIN = const(0)
BL_PIN = const(21)

# ==========================
# Touch configuration
# ==========================

TOUCH_BAUD_RATE = const(1000000)
TOUCH_SCK_PIN = const(25)
TOUCH_MOSI_PIN = const(32)
TOUCH_MISO_PIN = const(39)
TOUCH_CS_PIN = const(33)
TOUCH_INT_PIN = const(36)


# ==========================
# set up SPI for display
# ==========================

spi_display = SPI(1, baudrate=SPI1_BAUD_RATE, sck=Pin(SPI1_SCK_PIN), mosi=Pin(SPI1_MOSI_PIN))
display = Display(
        spi_display,
        dc=Pin(DISPLAY_DC_PIN),
        cs=Pin(DISPLAY_CS_PIN),
        rst=Pin(DISPLAY_RST_PIN),
        width=DISPLAY_WIDTH,
        height=DISPLAY_HEIGHT,
        rotation=ROTATION
)



# ==========================
# set up SPI for Touch
# ==========================

last_touch_x = None
last_touch_y = None

def touchscreen_press(x, y):
    global last_touch_x, last_touch_y
    last_touch_x = x
    last_touch_y = y
    print("Touch at", x, y)

def get_last_touch():
    return last_touch_x, last_touch_y
    

spi_touch = SPI(2, baudrate=TOUCH_BAUD_RATE, sck=Pin(TOUCH_SCK_PIN), mosi=Pin(TOUCH_MOSI_PIN), miso=Pin(TOUCH_MISO_PIN))
touch = Touch(
    spi_touch, 
    cs=Pin(33), 
    int_pin=Pin(36), 
    int_handler=touchscreen_press
)



# ==========================
# COLOR
# ==========================

# TO IMPORT: from lib.ili9341 import Display, color565

# to use: refer to cheat sheet for more info

colors = {
    "RED": (0, 0, 255),
    "GREEN": (0, 255, 0),
    "BLUE": (255, 0, 0),
    "YELLOW": (0, 255, 255),
    "AQUA": (255, 255, 0),
    "MAROON": (0, 0, 128),
    "DARK_GREEN": (0, 128, 0),
    "NAVY": (128, 0, 0),
    "TEAL": (0, 128, 128),
    "PURPLE": (128, 0, 128),
    "ORANGE": (0, 128, 255),
    "DEEP_PINK": (128, 0, 255),
    "CYAN": (255, 255, 128),
    "GREY": (128, 128, 128),
    "LIGHT_GREY": (192, 192, 192),
    "DARK_GREY": (64, 64, 64),
}
