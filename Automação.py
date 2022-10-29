import time
import pyautogui as py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(navegador)

n = navegador
ng = navegador.get
a = By.XPATH
f = navegador.find_element
t = time.sleep
nes = navegador.execute_script
nsw = navegador.switch_to.window

nes("window.open('about:blank','secondtab');")

nsw("secondtab")

ng('https://www.casaevideo.com.br/login?returnUrl=%2Flogin%3FreturnUrl%3D%252Flogin%253FreturnUrl%253D%25252Flogin%25253FreturnUrl%25253D%2525252F')
t(3)
f(a ,"//a[contains(text(), 'Não')]").click()
t(3)
n.execute_script("window.open('about:blank','thirdtab');")
nsw("thirdtab")
ng('https://www.mohmal.com/pt/inbox')
# f(a,'//a[contains(@id, "at-cv")]').click()
f(a,'//a[contains(@id, "delete")]').click()
f(a,'//div[contains(@class, "email")]').click()

t(3)

nsw("secondtab")
f(a,'//input[contains(@name, "email")]').click()
py.hotkey('ctrl','v')
py.press('enter')
t(3)
nsw("thirdtab")
n.refresh()
t(5)
#if  f(a,'//a[contains(@title, "Close")]')
# if navegador.find_element(By.CSS_SELECTOR,'#at-cv-lightbox-close'):
#     f(a,'//a[contains(@title, "Close")]').click()
# else:
#     pass

f(a,'//a[contains(text(), "Seu")]').click()
t(3)
# action = ActionChains(n)
# double = navegador.find_element(a,'//h1[contains(@style, "Margin")]');
# action.double_click(double).perform()

retornar = {"codigo" : "",};
page = navegador.find_element(a,'//h1[contains(@style, "Margin")]');
codigo = page.find_element(a,'//h1[contains(@style, "Margin")]')
for i in range(len(codigo)):
    retornar["codigo"] = retornar["codigo"] + codigo[i].text + " ";

pegoucode = [];
retornar = [];
for i in range(len(pegoucode)):
    retornar.append(pegoucode[i]);

#f(a,'//h1[contains(@style, "Margin")]').click()
py.hotkey('ctrl','c')
nsw("secondtab")
f(a,'//input[contains(@name, "token")]').click()
py.hotkey('ctrl','v')
f(a,'//input[contains(@type, "password")]').send_keys(password)

n.quit()