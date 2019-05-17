import board
import time
import neopixel

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (255, 100, 120)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
BLUE = (0, 0, 255)
LIGHT_BLUE = (80, 200, 175)
WHITE = (255, 255, 255)

BRIGHTNESS = .6

colors = [BLUE, RED, ORANGE, YELLOW, GREEN,
          CYAN, PURPLE, PINK, LIGHT_BLUE, WHITE]

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (g, r, b)

# NeoPixel setup
pixels_hour = neopixel.NeoPixel(board.D3, 15, brightness=BRIGHTNESS, auto_write=False)
pixels_minute = neopixel.NeoPixel(board.D4, 15, brightness=BRIGHTNESS,  auto_write=False)

pixels_hour.fill(BLACK)
pixels_minute.fill(BLACK)


def digit_1(value, color):
    if value == 0:
        # 0
        pixels_hour[8] = color
        pixels_hour[9] = color
        pixels_hour[10] = color
        pixels_hour[12] = color
        pixels_hour[13] = color
        pixels_hour[14] = color

    if value == 1:
        # 1
        pixels_hour[8] = color
        pixels_hour[12] = color

    if value == 2:
        # 2
        pixels_hour[8] = color
        pixels_hour[9] = color
        pixels_hour[11] = color
        pixels_hour[13] = color
        pixels_hour[14] = color

    if value == 3:
        # 3
        pixels_hour[8] = color
        pixels_hour[9] = color
        pixels_hour[11] = color
        pixels_hour[12] = color
        pixels_hour[13] = color

    if value == 4:
        # 4
        pixels_hour[8] = color
        pixels_hour[10] = color
        pixels_hour[11] = color
        pixels_hour[12] = color

    if value == 5:
        # 5
        pixels_hour[9] = color
        pixels_hour[10] = color
        pixels_hour[11] = color
        pixels_hour[12] = color
        pixels_hour[13] = color

    if value == 6:
        # 6
        pixels_hour[9] = color
        pixels_hour[10] = color
        pixels_hour[11] = color
        pixels_hour[12] = color
        pixels_hour[13] = color
        pixels_hour[14] = color

    if value == 7:
        # 7
        pixels_hour[8] = color
        pixels_hour[9] = color
        pixels_hour[12] = color

    if value == 8:
        # 8
        pixels_hour[8] = color
        pixels_hour[9] = color
        pixels_hour[10] = color
        pixels_hour[11] = color
        pixels_hour[12] = color
        pixels_hour[13] = color
        pixels_hour[14] = color

    if value == 9:
        # 9
        pixels_hour[8] = color
        pixels_hour[9] = color
        pixels_hour[10] = color
        pixels_hour[11] = color
        pixels_hour[12] = color
        pixels_hour[13] = color


def digit_2(value, color):
    if value == 0:
        # 0
        pixels_hour[1] = color
        pixels_hour[2] = color
        pixels_hour[3] = color
        pixels_hour[5] = color
        pixels_hour[6] = color
        pixels_hour[7] = color

    if value == 1:
        # 1
        pixels_hour[1] = color
        pixels_hour[5] = color

    if value == 2:
        # 2
        pixels_hour[1] = color
        pixels_hour[2] = color
        pixels_hour[4] = color
        pixels_hour[6] = color
        pixels_hour[7] = color

    if value == 3:
        # 3
        pixels_hour[1] = color
        pixels_hour[2] = color
        pixels_hour[4] = color
        pixels_hour[5] = color
        pixels_hour[6] = color

    if value == 4:
        # 4
        pixels_hour[1] = color
        pixels_hour[3] = color
        pixels_hour[4] = color
        pixels_hour[5] = color

    if value == 5:
        # 5
        pixels_hour[2] = color
        pixels_hour[3] = color
        pixels_hour[4] = color
        pixels_hour[5] = color
        pixels_hour[6] = color

    if value == 6:
        # 6
        pixels_hour[2] = color
        pixels_hour[3] = color
        pixels_hour[4] = color
        pixels_hour[5] = color
        pixels_hour[6] = color
        pixels_hour[7] = color

    if value == 7:
        # 7
        pixels_hour[1] = color
        pixels_hour[2] = color
        pixels_hour[5] = color

    if value == 8:
        # 8
        pixels_hour[1] = color
        pixels_hour[2] = color
        pixels_hour[3] = color
        pixels_hour[4] = color
        pixels_hour[5] = color
        pixels_hour[6] = color
        pixels_hour[7] = color

    if value == 9:
        # 9
        pixels_hour[1] = color
        pixels_hour[2] = color
        pixels_hour[3] = color
        pixels_hour[4] = color
        pixels_hour[5] = color
        pixels_hour[6] = color


def digit_3(value, color):
    if value == 0:
        # 0
        pixels_minute[1] = color
        pixels_minute[2] = color
        pixels_minute[3] = color
        pixels_minute[5] = color
        pixels_minute[6] = color
        pixels_minute[7] = color

    if value == 1:
        # 1
        pixels_minute[3] = color
        pixels_minute[7] = color

    if value == 2:
        # 2
        pixels_minute[1] = color
        pixels_minute[2] = color
        pixels_minute[4] = color
        pixels_minute[6] = color
        pixels_minute[7] = color

    if value == 3:
        # 3
        pixels_minute[3] = color
        pixels_minute[2] = color
        pixels_minute[4] = color
        pixels_minute[7] = color
        pixels_minute[6] = color

    if value == 4:
        # 4
        pixels_minute[7] = color
        pixels_minute[3] = color
        pixels_minute[4] = color
        pixels_minute[5] = color

    if value == 5:
        # 5
        pixels_minute[2] = color
        pixels_minute[3] = color
        pixels_minute[4] = color
        pixels_minute[5] = color
        pixels_minute[6] = color

    if value == 6:
        # 6
        pixels_minute[2] = color
        pixels_minute[3] = color
        pixels_minute[4] = color
        pixels_minute[5] = color
        pixels_minute[6] = color
        pixels_minute[1] = color

    if value == 7:
        # 7
        pixels_minute[3] = color
        pixels_minute[6] = color
        pixels_minute[7] = color

    if value == 8:
        # 8
        pixels_minute[1] = color
        pixels_minute[2] = color
        pixels_minute[3] = color
        pixels_minute[4] = color
        pixels_minute[5] = color
        pixels_minute[6] = color
        pixels_minute[7] = color

    if value == 9:
        # 9
        pixels_minute[7] = color
        pixels_minute[2] = color
        pixels_minute[3] = color
        pixels_minute[4] = color
        pixels_minute[5] = color
        pixels_minute[6] = color


def digit_4(value, color):
    if value == 0:
        # 0
        pixels_minute[8] = color
        pixels_minute[9] = color
        pixels_minute[10] = color
        pixels_minute[12] = color
        pixels_minute[13] = color
        pixels_minute[14] = color

    if value == 1:
        # 1
        pixels_minute[10] = color
        pixels_minute[14] = color

    if value == 2:
        # 2
        pixels_minute[8] = color
        pixels_minute[9] = color
        pixels_minute[11] = color
        pixels_minute[13] = color
        pixels_minute[14] = color

    if value == 3:
        # 3
        pixels_minute[10] = color
        pixels_minute[9] = color
        pixels_minute[11] = color
        pixels_minute[14] = color
        pixels_minute[13] = color

    if value == 4:
        # 4
        pixels_minute[14] = color
        pixels_minute[10] = color
        pixels_minute[11] = color
        pixels_minute[12] = color

    if value == 5:
        # 5
        pixels_minute[9] = color
        pixels_minute[10] = color
        pixels_minute[11] = color
        pixels_minute[12] = color
        pixels_minute[13] = color

    if value == 6:
        # 6
        pixels_minute[9] = color
        pixels_minute[10] = color
        pixels_minute[11] = color
        pixels_minute[12] = color
        pixels_minute[13] = color
        pixels_minute[8] = color

    if value == 7:
        # 7
        pixels_minute[10] = color
        pixels_minute[13] = color
        pixels_minute[14] = color

    if value == 8:
        # 8
        pixels_minute[8] = color
        pixels_minute[9] = color
        pixels_minute[10] = color
        pixels_minute[11] = color
        pixels_minute[12] = color
        pixels_minute[13] = color
        pixels_minute[14] = color

    if value == 9:
        # 9
        pixels_minute[14] = color
        pixels_minute[9] = color
        pixels_minute[10] = color
        pixels_minute[11] = color
        pixels_minute[12] = color
        pixels_minute[13] = color


def colons(color):
    pixels_hour[0] = color
    pixels_minute[0] = color


def clear():
    pixels_hour.fill(BLACK)
    pixels_minute.fill(BLACK)


def display(value, color):
    digits = str(value)
    digit_1(int(digits[0]), color)
    digit_2(int(digits[1]), color)
    digit_3(int(digits[2]), color)
    digit_4(int(digits[3]), color)


elapsed = 1000
color = RED

while True:
    print(elapsed)
    clear()
    time.sleep(1)
    colons(color)
    display(elapsed, color)
    pixels_hour.show()
    pixels_minute.show()
    elapsed += 1
