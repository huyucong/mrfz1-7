from ctypes import *
import pyautogui
import time

# 设置反应时间
time.sleep(5)
while 1:
    # 挑战位置按钮的点击
    pyautogui.click(1713, 984)
    time.sleep(6)
    # 确认挑战按钮的点击
    pyautogui.click(1659, 731)
    time.sleep(90)
    # 跳过结算界面的点击
    pyautogui.click(1659, 510)
    time.sleep(8)
