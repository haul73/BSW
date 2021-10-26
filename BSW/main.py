import win32gui
from PIL import Image, ImageGrab
import time

box = (0, 0, 1000, 600)
target = (915, 50, 950, 85)


def SetNoxWindow(x):
    hwnd = win32gui.FindWindow(None, "NoxPlayer")
    if hwnd != 0:
        win32gui.MoveWindow(hwnd, x[0], x[1], x[2], x[3], True)
        print("Окно установлено")
    else:
        print("Окно не найдено")


def makeHash(grab, target):
    screenshot = ImageGrab.grab(grab)  # Делаем скриншот игры
    crops = screenshot.crop(target)  # Обрезаем по цели
    newSize = (8, 8)  # Уменьшаем
    crops = crops.resize(newSize)
    crops = crops.convert("L")  # Убираем цвет
    pix = crops.load()  # Запускаем доступ к пикселям
    sum = 0  # Выясняем среднюю сумму
    for i in range(8):
        for b in range(8):
            sum = sum + pix[i, b]
    sum = round(sum / 64)
    print(sum)
    hash=""
    for i in range(8):  # Преобразовываем в  0 и 1
        for b in range(8):
            if pix[i, b] >= sum:
                pix[i, b] = 1
            else:
                pix[i, b] = 0
            hash = hash + str(pix[i, b])
    hash=hex(int(hash, 2))
    return hash


time.sleep(3)
SetNoxWindow(box)
a=makeHash(box, target)
print(a)

