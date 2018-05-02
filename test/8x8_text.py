import RPi.GPIO as gpio
import time

def setupAll():
    gpio.setmode(gpio.BCM)
    global col_led, row_led
    for i in col_led + row_led:
        try:
            gpio.setup(i, gpio.OUT)
        except:
            print(str(i) + "wasn't be setuped.")
def cleanAll():
    global col_led, row_led
    for i in row_led:
        gpio.output(i, gpio.LOW)
    for i in col_led:
        gpio.output(i, gpio.HIGH)
    gpio.cleanup()

def show8x8(image):
    for i in col_led:
        gpio.output(i, gpio.HIGH)

    # for i in range(len(image)):
    #     for j in range(len(image[i])):
    #         if image[i][j]:
    #             gpio.output(row_led[])


col_led = [17, 27, 22, 5, 6, 13, 19, 26]
row_led = [15, 18, 23, 24, 12, 16, 20, 21]

if __name__ == '__main__':
    try:
        setupAll()

        temp1 = [0, 1]
        temp2 = [1, 0]
        icon = [temp1 * 4, temp2 * 4] * 4

        print(icon)

        for _ in range(10):
            for i in range(8):
                gpio.output(row_led[i], gpio.HIGH)
                gpio.output(col_led[i], gpio.LOW)
                time.sleep(0.05)
                gpio.output(col_led[i], gpio.HIGH)
        for _ in range(20):
            for i in range(8):
                gpio.output(row_led[i], gpio.HIGH)
                gpio.output(col_led[i], gpio.LOW)
                time.sleep(0.01)
                gpio.output(col_led[i], gpio.HIGH)
        for _ in range(100):
            for i in range(8):
                gpio.output(row_led[i], gpio.HIGH)
                gpio.output(col_led[i], gpio.LOW)
                time.sleep(0.002)
                gpio.output(col_led[i], gpio.HIGH)

        # for i in col_led[0:5]:
        #     gpio.output(i, gpio.LOW)
        # for i in row_led[0:3]:
        #     gpio.output(i, gpio.HIGH)

        time.sleep(10)
    finally:
        cleanAll()
