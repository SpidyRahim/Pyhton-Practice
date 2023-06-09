import pyautogui
import time


def auto_pyramid(n):
    time.sleep(5)
    for i in range(1, n+1):
        for j in range(0, i):
            pyautogui.write('#', interval=0.25)

        pyautogui.press('enter')


n = int(input())

auto_pyramid(n)