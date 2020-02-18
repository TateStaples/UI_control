from pynput_engine import keyboard
from time import sleep


def spam():
    for i in range(100):
        sleep(.01)
        keyboard.type("Hi there Jet.")
        keyboard.type("\n")
        print(i)


if __name__ == '__main__':
    keyboard.on_press(keyboard.keys.cmd_l, spam)
    while True:
        sleep(1000)