import pyautogui as pt
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyboardController
from time import sleep

pt.FAILSAFE = True
mouse = Controller()
keyboard = KeyboardController()

def check_message():
    position = pt.locateCenterOnScreen('whatsapp_bot/image/circle.png',grayscale=False, confidence=.8)

    success = True
    if position is None:
        success = False
        print("image is not found.")
    return success

def reset():
    pt.moveTo(120, 124, duration=0.5)
    mouse.click(Button.left, 1)
    pt.typewrite('only')
    pt.moveTo(174, 254, duration=0.5)
    mouse.click(Button.left, 1)
    pt.moveTo(120, 124, duration=0.5)
    mouse.click(Button.left, 1)
    keyboard.press(Key.esc)

power = True
reply_message = "Sorry I am not able to reply you now, please leave your message here and I will reply you asap!\n --Auto Reply Bot\n"
sleep(5)
while power:
    x = 127
    y = 200
    success = check_message()
    while success:
        pt.moveTo(x, y, duration = 0.5)
        mouse.click(Button.left, 1)
        pt.moveTo(587, 953, duration = 0.3)
        mouse.click(Button.left, 1)
        pt.typewrite(reply_message, interval=0.0)
        y += 73
        if y > 440:
            break
        success = check_message()
    reset()
    sleep(10)
