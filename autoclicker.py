from pynput_engine import keyboard, mouse
from time import sleep

if __name__ == '__main__':
    hold = False
    just_hit = False
    while True:
        sleep(.001)  # was 0.009
        if keyboard.is_pressed(keyboard.keys.backspace) or hold:
            mouse.click(1)
        test = keyboard.is_pressed(keyboard.keys.enter)
        if test and not just_hit:
            hold = not hold
            print(hold)
        just_hit = test

