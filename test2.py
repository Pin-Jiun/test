import random
from re import X
import matplotlib.pyplot as plt
import cv2
import ddddocr
import pytest
import time
import json
import os
import wget
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule

from datetime import datetime

time_goal = datetime.strptime('04:59:59',"%H:%M:%S")
currentTime = datetime.now().strftime("%H:%M:%S")
time_now = datetime.strptime(currentTime,"%H:%M:%S")
difference_sec = (time_goal-time_now).seconds
print("離搶場時間大約還有",difference_sec,"秒")
print("waiting...")
# time.sleep(difference_sec-360)
print("working...")

week_list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
week = week_list[datetime.now().weekday()]
print(type(week))

print("test4")
