import time;
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from webdriver_manager.chrome import ChromeDriverManager;
from selenium.webdriver.common.action_chains import ActionChains;
navegador = webdriver.Chrome(ChromeDriverManager().install());
action = ActionChains(navegador);

navegador.get("https://www.casaevideo.com.br/login?returnUrl=%2Flogin%3FreturnUrl%3D%252Flogin%253FreturnUrl%253D%25252Flogin%25253FreturnUrl%25253D%2525252F");
navegador.execute_script("window.open('about:blank','secondtab');");

navegador.switch_to.window('secondtab');
navegador.get('https://www.mohmal.com/pt/inbox');
time.sleep(50)
navegador.close();

