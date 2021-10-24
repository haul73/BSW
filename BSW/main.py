import pyautogui as pg
import pprint
import win32gui
import win32con


def SetNoxWindow(x=0, y=0, cx=800, cy=400):
    hwnd = win32gui.FindWindow(None, "NoxPlayer")
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, x, y, cx, cy, True)
        print("Окно установлено")
    else:
        print("Окно не найдено")


SetNoxWindow()
