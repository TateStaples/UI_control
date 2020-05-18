from random import randint
from pynput_engine import mouse, keyboard
from time import sleep

if __name__ == '__main__':
    while True:
        if keyboard.is_pressed(keyboard.keys.enter):
            mouse.right_click(2)