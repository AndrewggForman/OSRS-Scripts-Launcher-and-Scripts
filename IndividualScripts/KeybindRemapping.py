import keyboard
import pyautogui    

def click():
    pyautogui.click()

while True:
    if(keyboard.is_pressed('0')):
       click()