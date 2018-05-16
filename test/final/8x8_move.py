import HC595_one
import RPi.GPIO as gpio

def display():
    data = [
        '00011000',
        '00111100',
        '01111110',
        '11111111',
        '11100111',
        '11000011',
        '10000001',
        '00000000'
    ]

    # for line in data:
    #     print([int(b) for b in line])
    b_data = [[int(b) for b in line] for line in data] * 3
    print(b_data)
    HC595_one.hc_out(b_data, 0.5)

if __name__ == '__main__':
    try:
        HC595_one.setup()
        display()
    finally:
        gpio.cleanup()
