import pynput
import _thread


class Mouse:
    _Button = pynput.mouse.Button
    left = _Button.left
    right = _Button.right
    middle = _Button.middle
    click_actions = []
    scroll_actions = []
    move_actions = []

    def __init__(self):
        self._Listener = pynput.mouse.Listener(on_click=self._on_click, on_move=self._on_move, on_scroll=self._on_scroll)
        self._Controller = pynput.mouse.Controller()
        self._Listener.start()

    # controller
    def goto(self, x, y):
        self._Controller.position = x, y

    def drag(self, x1, y1, x2, y2):
        self.goto(x1, y1)
        self.hold()
        self.goto(x2, y2)
        self.release()

    def hold(self):
        self._Controller.press(self.left)

    def release(self):
        self._Controller.release(self.left)

    def click(self, amount=1):
        self._Controller.click(self.left, amount)

    def right_click(self, amount=1):
        for i in range(amount):
            self._Controller.click(self.right)

    def middle_click(self, amount=1):
        for i in range(amount):
            self._Controller.click(self.middle)

    def scroll_up(self, amount):
        self._Controller.scroll(0, -amount)

    def scroll_down(self, amount):
        self._Controller.scroll(0, amount)

    def scroll_side(self, amount):
        self._Controller.scroll(amount, 0)

    def move(self, dx=0, dy=0):
        self._Controller.move(dx, dy)

    # Listener
    def position(self):
        return self._Controller.position

    def alter_listener(self, move=None, click=None, scroll=None):
        move = self._on_move if move is None else move
        click = self._on_click if click is None else click
        scroll = self._on_scroll if scroll is None else scroll
        del self._Listener
        self._Listener = pynput.mouse.Listener(move, click, scroll)
        self._Listener.start()

    @staticmethod
    def _on_click(x, y, button, pressed):
        Mouse.click_actions.append((x, y))

    @staticmethod
    def _on_move(x, y):
        Mouse.move_actions.append((x, y))

    @staticmethod
    def _on_scroll(x, y, dx, dy):
        Mouse.scroll_actions.append((dx, dy))


class Keyboard:
    keys = pynput.keyboard.Key
    code = pynput.keyboard.KeyCode
    pressed_keys = set()
    press_actions = {}
    release_actions = {}

    def __init__(self):
        self._Listener = pynput.keyboard.Listener(on_press=self._on_press, on_release=self._on_release)
        self._Controller = pynput.keyboard.Controller()
        self._Listener.start()
        self.press_actions[str(self.keys.esc)] = self._quit

    # Controller
    def press(self, key):
        self._Controller.press(key)

    def release(self, key):
        self._Controller.release(key)

    def tap(self, key):
        self.press(key)
        self.release(key)

    def type(self, msg):
        self._Controller.type(str(msg))

    # Listener
    def get_pressed(self):
        return list(self.pressed_keys)

    def is_pressed(self, key):
        return key in self.pressed_keys

    def clear_history(self):
        self.pressed_keys = set()

    def on_press(self, key, func):
        key = str(key)
        self.press_actions[key] = func

    def on_release(self, key, func):
        key = str(key)
        self.release_actions[key] = func

    @staticmethod
    def _on_press(key):
        Keyboard.pressed_keys.add(key)
        key = str(key)
        try:
            if key in Keyboard.press_actions:
                Keyboard.press_actions[key]()
        except KeyError:
            pass

    @staticmethod
    def _on_release(key):
        Keyboard.pressed_keys.remove(key)
        key = str(key)
        try:
            if key in Keyboard.press_actions:
                Keyboard.press_actions[key]()
        except KeyError:
            pass

    @staticmethod
    def _quit():
        _thread.interrupt_main()


mouse = Mouse()
keyboard = Keyboard()
