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
pixels_minutes = neopixel.NeoPixel(board.D3, 15, brightness=BRIGHTNESS, auto_write=False)
pixels_seconds = neopixel.NeoPixel(board.D4, 15, brightness=BRIGHTNESS,  auto_write=False)

pixels_minutes.fill(BLACK)
pixels_seconds.fill(BLACK)


def digit_1(value, color):
    if value == 0:
        # 0
        pixels_minutes[8] = color
        pixels_minutes[9] = color
        pixels_minutes[10] = color
        pixels_minutes[12] = color
        pixels_minutes[13] = color
        pixels_minutes[14] = color

    if value == 1:
        # 1
        pixels_minutes[8] = color
        pixels_minutes[12] = color

    if value == 2:
        # 2
        pixels_minutes[8] = color
        pixels_minutes[9] = color
        pixels_minutes[11] = color
        pixels_minutes[13] = color
        pixels_minutes[14] = color

    if value == 3:
        # 3
        pixels_minutes[8] = color
        pixels_minutes[9] = color
        pixels_minutes[11] = color
        pixels_minutes[12] = color
        pixels_minutes[13] = color

    if value == 4:
        # 4
        pixels_minutes[8] = color
        pixels_minutes[10] = color
        pixels_minutes[11] = color
        pixels_minutes[12] = color

    if value == 5:
        # 5
        pixels_minutes[9] = color
        pixels_minutes[10] = color
        pixels_minutes[11] = color
        pixels_minutes[12] = color
        pixels_minutes[13] = color

    if value == 6:
        # 6
        pixels_minutes[9] = color
        pixels_minutes[10] = color
        pixels_minutes[11] = color
        pixels_minutes[12] = color
        pixels_minutes[13] = color
        pixels_minutes[14] = color

    if value == 7:
        # 7
        pixels_minutes[8] = color
        pixels_minutes[9] = color
        pixels_minutes[12] = color

    if value == 8:
        # 8
        pixels_minutes[8] = color
        pixels_minutes[9] = color
        pixels_minutes[10] = color
        pixels_minutes[11] = color
        pixels_minutes[12] = color
        pixels_minutes[13] = color
        pixels_minutes[14] = color

    if value == 9:
        # 9
        pixels_minutes[8] = color
        pixels_minutes[9] = color
        pixels_minutes[10] = color
        pixels_minutes[11] = color
        pixels_minutes[12] = color
        pixels_minutes[13] = color


def digit_2(value, color):
    if value == 0:
        # 0
        pixels_minutes[1] = color
        pixels_minutes[2] = color
        pixels_minutes[3] = color
        pixels_minutes[5] = color
        pixels_minutes[6] = color
        pixels_minutes[7] = color

    if value == 1:
        # 1
        pixels_minutes[1] = color
        pixels_minutes[5] = color

    if value == 2:
        # 2
        pixels_minutes[1] = color
        pixels_minutes[2] = color
        pixels_minutes[4] = color
        pixels_minutes[6] = color
        pixels_minutes[7] = color

    if value == 3:
        # 3
        pixels_minutes[1] = color
        pixels_minutes[2] = color
        pixels_minutes[4] = color
        pixels_minutes[5] = color
        pixels_minutes[6] = color

    if value == 4:
        # 4
        pixels_minutes[1] = color
        pixels_minutes[3] = color
        pixels_minutes[4] = color
        pixels_minutes[5] = color

    if value == 5:
        # 5
        pixels_minutes[2] = color
        pixels_minutes[3] = color
        pixels_minutes[4] = color
        pixels_minutes[5] = color
        pixels_minutes[6] = color

    if value == 6:
        # 6
        pixels_minutes[2] = color
        pixels_minutes[3] = color
        pixels_minutes[4] = color
        pixels_minutes[5] = color
        pixels_minutes[6] = color
        pixels_minutes[7] = color

    if value == 7:
        # 7
        pixels_minutes[1] = color
        pixels_minutes[2] = color
        pixels_minutes[5] = color

    if value == 8:
        # 8
        pixels_minutes[1] = color
        pixels_minutes[2] = color
        pixels_minutes[3] = color
        pixels_minutes[4] = color
        pixels_minutes[5] = color
        pixels_minutes[6] = color
        pixels_minutes[7] = color

    if value == 9:
        # 9
        pixels_minutes[1] = color
        pixels_minutes[2] = color
        pixels_minutes[3] = color
        pixels_minutes[4] = color
        pixels_minutes[5] = color
        pixels_minutes[6] = color


def digit_3(value, color):
    if value == 0:
        # 0
        pixels_seconds[1] = color
        pixels_seconds[2] = color
        pixels_seconds[3] = color
        pixels_seconds[5] = color
        pixels_seconds[6] = color
        pixels_seconds[7] = color

    if value == 1:
        # 1
        pixels_seconds[3] = color
        pixels_seconds[7] = color

    if value == 2:
        # 2
        pixels_seconds[1] = color
        pixels_seconds[2] = color
        pixels_seconds[4] = color
        pixels_seconds[6] = color
        pixels_seconds[7] = color

    if value == 3:
        # 3
        pixels_seconds[3] = color
        pixels_seconds[2] = color
        pixels_seconds[4] = color
        pixels_seconds[7] = color
        pixels_seconds[6] = color

    if value == 4:
        # 4
        pixels_seconds[7] = color
        pixels_seconds[3] = color
        pixels_seconds[4] = color
        pixels_seconds[5] = color

    if value == 5:
        # 5
        pixels_seconds[2] = color
        pixels_seconds[3] = color
        pixels_seconds[4] = color
        pixels_seconds[5] = color
        pixels_seconds[6] = color

    if value == 6:
        # 6
        pixels_seconds[2] = color
        pixels_seconds[3] = color
        pixels_seconds[4] = color
        pixels_seconds[5] = color
        pixels_seconds[6] = color
        pixels_seconds[1] = color

    if value == 7:
        # 7
        pixels_seconds[3] = color
        pixels_seconds[6] = color
        pixels_seconds[7] = color

    if value == 8:
        # 8
        pixels_seconds[1] = color
        pixels_seconds[2] = color
        pixels_seconds[3] = color
        pixels_seconds[4] = color
        pixels_seconds[5] = color
        pixels_seconds[6] = color
        pixels_seconds[7] = color

    if value == 9:
        # 9
        pixels_seconds[7] = color
        pixels_seconds[2] = color
        pixels_seconds[3] = color
        pixels_seconds[4] = color
        pixels_seconds[5] = color
        pixels_seconds[6] = color


def digit_4(value, color):
    if value == 0:
        # 0
        pixels_seconds[8] = color
        pixels_seconds[9] = color
        pixels_seconds[10] = color
        pixels_seconds[12] = color
        pixels_seconds[13] = color
        pixels_seconds[14] = color

    if value == 1:
        # 1
        pixels_seconds[10] = color
        pixels_seconds[14] = color

    if value == 2:
        # 2
        pixels_seconds[8] = color
        pixels_seconds[9] = color
        pixels_seconds[11] = color
        pixels_seconds[13] = color
        pixels_seconds[14] = color

    if value == 3:
        # 3
        pixels_seconds[10] = color
        pixels_seconds[9] = color
        pixels_seconds[11] = color
        pixels_seconds[14] = color
        pixels_seconds[13] = color

    if value == 4:
        # 4
        pixels_seconds[14] = color
        pixels_seconds[10] = color
        pixels_seconds[11] = color
        pixels_seconds[12] = color

    if value == 5:
        # 5
        pixels_seconds[9] = color
        pixels_seconds[10] = color
        pixels_seconds[11] = color
        pixels_seconds[12] = color
        pixels_seconds[13] = color

    if value == 6:
        # 6
        pixels_seconds[9] = color
        pixels_seconds[10] = color
        pixels_seconds[11] = color
        pixels_seconds[12] = color
        pixels_seconds[13] = color
        pixels_seconds[8] = color

    if value == 7:
        # 7
        pixels_seconds[10] = color
        pixels_seconds[13] = color
        pixels_seconds[14] = color

    if value == 8:
        # 8
        pixels_seconds[8] = color
        pixels_seconds[9] = color
        pixels_seconds[10] = color
        pixels_seconds[11] = color
        pixels_seconds[12] = color
        pixels_seconds[13] = color
        pixels_seconds[14] = color

    if value == 9:
        # 9
        pixels_seconds[14] = color
        pixels_seconds[9] = color
        pixels_seconds[10] = color
        pixels_seconds[11] = color
        pixels_seconds[12] = color
        pixels_seconds[13] = color


def colons(color):
    pixels_minutes[0] = color
    pixels_seconds[0] = color


def clear():
    pixels_minutes.fill(BLACK)
    pixels_seconds.fill(BLACK)


def convert_time(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return "%02d%02d" % (min, sec)


def display(value, color):
    digits = convert_time(value)
    digit_1(int(digits[0]), color)
    digit_2(int(digits[1]), color)
    digit_3(int(digits[2]), color)
    digit_4(int(digits[3]), color)


elapsed = 0000
# color = RED

while True:
    print(elapsed)
    color = wheel(elapsed & 255)
    clear()
    time.sleep(1)
    colons(color)
    display(elapsed, color)
    pixels_minutes.show()
    pixels_seconds.show()
    elapsed += 1
