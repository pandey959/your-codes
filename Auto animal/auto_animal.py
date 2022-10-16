import pyautogui as pg
import time

time.sleep(10)
txt=open('animals.txt')

a='You are'
for animal in txt:
    pg.write(a+' '+ animal)
    pg.press('Enter')