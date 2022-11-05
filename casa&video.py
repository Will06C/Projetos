from browser import *;

class CasaEvideo(Browser):
    def __init__(self):
        super().__init__();
        self.navegador.get('https://www.casaevideo.com.br/login?returnUrl=%2Flogin%3FreturnUrl%3D%252Flogin%253FreturnUrl%253D%25252Flogin%25253FreturnUrl%25253D%2525252F');
        self.navegador.find_element(By.XPATH,"//a[contains(text(), 'Não')]").click();
        self.navegador.execute_script("window.open('about:blank','secondtab');");
        self.navegador.switch_to.window("secondtab");
        self.navegador.get('https://www.mohmal.com/pt/inbox');
        




