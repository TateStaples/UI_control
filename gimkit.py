import requests
from bs4 import *
from pynput_engine import mouse

topleft = None
topright = None
bottomleft = None
bottomright = None


def get_question():
    return soup.find_all(class_ = "notranslate lang-en")


def get_answers():
    pass


def click_answer(number):
    mouse.goto(*(topleft, topright, bottomleft, bottomright)[number])
    mouse.click()


if __name__ == '__main__':
    url = input("What is the url?:   ").strip()
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.content, "lxml")
    print(get_question())