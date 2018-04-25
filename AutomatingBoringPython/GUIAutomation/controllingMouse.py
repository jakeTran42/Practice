import pyautogui

size = pyautogui.size() #getting screen size

width, height = size

pyautogui.position() #current mouse coordinates

pyautogui.moveTo(10,10) #moving mouse cursor

pyautogui.moveTo(10, 10, duration=1.5) #moving mouse slowly

pyautogui.moveRel(200, 0) #moving mouse relatively to current position

pyautogui.click(643, 216)
