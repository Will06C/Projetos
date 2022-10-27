import random
import time
from random import sample
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#navegador.get('https://temp-mail.org/pt/')   - BLOQUENANDO CHROME AUTOMATIZADO
#navegador.get('https://www.mohmal.com/pt/inbox')
navegador.get('https://www.mohmal.com/pt/inbox')

navegador.find_element(By.XPATH ,'//*[@id="delete"]').click()

navegador.find_element(By.XPATH ,'//*[@id="email"]/div[1]').click()
#************************************************************#

#nomes = ['names']     TENTANDO UM NOME E SOBRENOME ALEATORIO
#                                DA LISTA DO EXCEL 
#for nome in nomes:
    #print(nome)
    #tabela = pd.read_excel(f'{nome}.xlsx')
    #print(tabela)
    #sobrenome = tabela.loc[tabela['SOBRENOME']].values[0]
    #nome = tabela.loc[tabela['NAME']].values[0]
    #print(f'{NAME},{SOBRENOME}')
    #print(random.choices([tabela]))


#***************************************************************#

nomes = ['Jose', 'Bruno', 'Lucas', 'Eduardo', 'Pedro', 'Luciano', 'Vitor', 'Diego', 'Rômulo',
'Carlinhos', 'Carlos', 'Davi', 'Thiago', 'Paulo', 'Igor', 'Felipe', 'Marcelo', 'Matheus', 'Fabio',
'Artur', 'Anderson', 'Gustavo', 'Rogerio', 'Marcus', 'Nando', 'Jorge', 'Rodrigo', 'Caio', 'Jonas',]

sobrenome = ['Jose', 'Bruno', 'Lucas', 'Eduardo', 'Pedro', 'Luciano', 'Vitor', 'Diego', 'Rômulo',
'Carlinhos', 'Carlos', 'Davi', 'Thiago', 'Paulo', 'Igor', 'Felipe', 'Marcelo', 'Matheus', 'Fabio',
'Artur', 'Anderson', 'Gustavo', 'Rogerio', 'Marcus', 'Nando', 'Jorge', 'Rodrigo', 'Caio', 'Jonas',]

(random.choice(nomes))
(random.choice(sobrenome))
#(random.randint('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'))
#(random.choice('1','2','3','4','5','6'))

#a = (By.XPATH)
#b = navegador.find_element
#navegador.find_element(By.XPATH,'//*[@id="click-to-change"]').click()

#time.sleep

#navegador.find_element(By.XPATH,'//*[@id="new_mail"]').send_keys(nomes,sobrenome)

#navegador.find_element(a ,'//*[@id="delete"]').click()

#navegador.find_element(a ,'//*[@id="email"]/div[1]').click()

navegador.get('https://www.facebook.com/')

time.sleep(10)

navegador.find_element(By.XPATH , '//*[@id="u_0_0_uV"]').click()

navegador.find_element(By.XPATH , '//*[@id="u_4_b_+u"]').click()

navegador.find_element(By.XPATH , '//*[@id="u_4_b_+u"]').send_keys((random.choice(nomes)))

navegador.find_element(By.XPATH , '//*[@id="u_u_d_gN"]').click()

navegador.find_element(By.XPATH , '//*[@id="u_u_d_gN"]').send_keys((random.choice(sobrenome)))

navegador.find_element(By.XPATH , '//*[@id="u_4_g_q2"]').click()

navegador.find_element(By.XPATH , '//*[@id="u_4_g_q2"]').send_keys('ctrl'+'v')

navegador.find_element(By.XPATH , '//*[@id="password_step_input"]').click()

(random.randint('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'))
(random.choice('1','2','3','4','5','6'))

navegador.find_element(By.XPATH , '//*[@id="password_step_input"]').send_keys((random.randint(random.randint)(random.randint)(random.randint(random.randint)(random.randint)(random.choice)(random.choice)(random.choice)(random.choice)(random.choice)(random.choice)(random.choice)(random.choice)(random.choice))))



time.sleep(100000)




    
