import pyautogui
import time
import os


def press_ctrl(t_min):
    t_sec = int(t_min * 60)  # Total seconds, ensure it's an integer

    while True:
        os.system('cls')  # Clear the console window
        print('\n\n')
        for remaining in range(t_sec, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer = '\tPress Ctrl in {:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")  # Print the timer and return to the start of the line
            time.sleep(1)

        pyautogui.hotkey('ctrl')  # Press the 'Ctrl' key


press_ctrl(2.9)
