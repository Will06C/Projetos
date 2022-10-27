import random as r
import time
import pyautogui as py
from random import sample
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

a = By.XPATH

f = navegador.find_element


navegador.get('https://www.casaevideo.com.br/')

time.sleep(5)

f(a , "//div[contains(@class, 'casaevideonewio-store-theme-5-x-rightTopContent')]/../..//div[contains(@class, 'vtex-login-2-x-container flex items-center fr')]").click()




time.sleep(1000)






