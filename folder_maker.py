from pynput_engine import mouse, keyboard
from time import sleep

# makes empty folders in google drive

# constants

new_button = (104, 186)
new_folder = (104, 186)
create = (846, 540)
create_leave = (878, 432)
info = (1347, 165)
parent = (1246, 645)
leave_info = (1345, 233)
depth = 3
cols = 4
rows = 10
folders_per_layer = 2
x_positions = [373, 639, 886, 1136]
y_positions = [277, 341, 397, 473, 537, 593, 669, 717, 776, 852]


def create_folder():
    sleep(1)
    click(*new_button, 3)
    sleep(.5)
    mouse.click(3)
    click(*create)
    sleep(1)
    # click(*create_leave)


def fill(amount):
    for folder in range(amount):
        create_folder()


def stuff(layers_remaining):
    sleep(1)
    fill(folders_per_layer)
    layers_remaining -= 1
    if layers_remaining > 0:
        for f in range(folders_per_layer):
            enter_folder(f)
            stuff(layers_remaining)
            backtrack()


def enter_folder(number):
    r = number // cols
    c = number % cols
    x = x_positions[c]
    y = y_positions[r]
    click(x, y, 2)


def backtrack():
    sleep(2)
    click(*info)
    sleep(3)
    click(*parent)
    sleep(2)
    click(*leave_info)


def click(x, y, amount=1):
    mouse.goto(x, y)
    sleep(.1)
    mouse.click(amount)


if __name__ == '__main__':
    sleep(3)
    stuff(depth)