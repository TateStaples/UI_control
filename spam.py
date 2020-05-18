from pynput_engine import keyboard
from time import sleep


def spam():
    with open("bee_movie_script.txt") as file:
        for line in file:
            if len(line) > 1:
                keyboard.type(line)
                sleep(10)

if __name__ == '__main__':
    keyboard.on_press(keyboard.keys.cmd_l, spam)
    while True: pass