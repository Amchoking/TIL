import pyautogui as pag
from PIL import ImageGrab
from tkinter import *
import keyboard
import webbrowser
import time

isrunning=False

def open_lilpa():
    webbrowser.open("https://www.twitch.tv/lilpaaaaaa")

def putmoney(money): #금액 입
    if(money==2000):
        keyboard.press('2')
    else:
        keyboard.press('1')
    for i in range(3):
        keyboard.press('0')
        time.sleep(0.5)
    time.sleep(1)

def autoto(): #1회 오토 토토
    money=0
    isleft=False
    while True:
        screen = ImageGrab.grab()
        rgb = screen.getpixel((2476, 219))
        if(rgb == (145, 71, 255)):
            break
        time.sleep(5)
    time.sleep(1)
    pag.click((2253, 1378))
    time.sleep(1)
    screen = ImageGrab.grab()
    left = screen.getpixel((2487, 1138))
    middle = screen.getpixel((2503, 1138))
    right = screen.getpixel((2519, 1139))
    if(middle == (224, 0, 142)):
        if(left == (224, 0, 142)):
            money=2000
        else:
            money=1000
        isleft=False
    else:
        if(right == (31, 105, 255)):
            money=2000
        else:
            money=1000
        isleft=True
    pag.click((2278, 1128))
    time.sleep(1)
    pag.click((2376, 1331))
    time.sleep(1)
    if(isleft):
        pag.click((2300, 1292))
        putmoney(money)
        pag.click((2366, 1284))
    else:
        pag.click((2418, 1286))
        putmoney(money)
        pag.click((2501, 1284))
    while True:
        screen = ImageGrab.grab()
        rgb = screen.getpixel((2476, 219))
        if(rgb != (145, 71, 255)):
            break
        time.sleep(5)
    pag.click((2523, 1062))

root = Tk()
root.title("Twitch Autoto")
root.geometry("180x170")
root.resizable(False,False)
btn_go = Button(root,text="릴파넴 방송가기",padx=20,pady=20,command = open_lilpa)
btn_go.grid(row = 0,column = 0, sticky=N+E+W+S,padx=20,pady=10)
btn=Button(root, text="무지성 정배 시작",padx=20,pady=20,command=autoto)
btn.grid(row = 1,column = 0, sticky=N+E+W+S,padx=20,pady=10)
root.mainloop()
