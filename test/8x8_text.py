import RPi.GPIO as gpio

def setupAll():
    global col_led, row_led
    for i in col_led + row_led:
        gpio.setup(i, gpio.OUT)

col_led = [17, 27, 22, 5, 6, 13, 19, 26]
row_led = [14, 15, 18, 23, 12, 16, 20, 21]

if __name__ == '__main__':
    try:
        setupAll()
    except:
        gpio.cleanup()
