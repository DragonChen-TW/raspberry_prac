import spidev
import time

def readadc(adc_num):
    print('adc_num is', adc_num)
    if adc_num > 7 or adc_num < 0:
        return -1
    global spi
    r = spi.xfer2([1, 8 + adc_num << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

if __name__ == '__main__':
    # Global Variable
    delay = 2
    LDR_channel = 0

    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 1000000

    while True:
        LDR_value = readadc(LDR_channel)
        print('-------------------')
        print("LDR value is",LDR_value)
        time.sleep(delay)
