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

BRIGHTNESS = .3

colors = [PINK, RED, ORANGE, YELLOW, GREEN,
          CYAN, PURPLE, BLUE, LIGHT_BLUE, WHITE]

# NeoPixel setup
pixels_hour = neopixel.NeoPixel(board.D1, 15, brightness=BRIGHTNESS)
pixels_minute = neopixel.NeoPixel(board.D2, 15, brightness=BRIGHTNESS)

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


colons(BLACK)



while True:
    for i in range(10):
        digit_1(i, colors[i])
        digit_2(i, colors[i])
        digit_3(i, colors[i])
        digit_4(i, colors[i])
        time.sleep(1)
        clear()




