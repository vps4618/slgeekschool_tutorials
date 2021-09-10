import pyautogui
import time
f=open("New Text Document.txt",'r')
time.sleep(1)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("Enter")