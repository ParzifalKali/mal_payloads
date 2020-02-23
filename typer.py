import pyautogui
import sys

word_to_type = sys.argv[1]
print(word_to_type)

for letter in word_to_type:
    pyautogui.keyDown(letter)

pyautogui.keyDown("Enter")
