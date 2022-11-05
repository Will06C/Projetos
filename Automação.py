import time
from utils import password
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

navegador.execute_script("window.open('about:blank','secondtab');");

navegador.switch_to.window("secondtab");

ng('https://www.casaevideo.com.br/login?returnUrl=%2Flogin%3FreturnUrl%3D%252Flogin%253FreturnUrl%253D%25252Flogin%25253FreturnUrl%25253D%2525252F');
t(3);
f(a ,"//a[contains(text(), 'Não')]").click();
t(3);
n.execute_script("window.open('about:blank','thirdtab');");
nsw("thirdtab");
ng('https://www.mohmal.com/pt/inbox');

f(a,'//a[contains(@id, "delete")]').click();
f(a,'//div[contains(@class, "email")]').click();
t(1)
nsw("secondtab");
t(1)
f(a,'//input[contains(@name, "email")]').click();
action.key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).send_keys(Keys.RETURN).perform();
t(4)
nsw("thirdtab");
n.refresh();
t(2);

f(a,'//a[contains(text(), "Seu")]').click()
t(3)

double = f(a,"/html/body/div/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/h1");
action = ActionChains(n)
action.double_click(double).perform()
action.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()
nsw("secondtab")
f(a,'//input[contains(@name, "token")]').click();
action.key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform()

f(a,'//input[contains(@type, "password")]').send_keys(password)
f(a,'//input[contains(@type, "password")]').text()
f(a,'//input[contains(@placeholder, "Confirmar")]').click();
action.key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform();


n.quit()