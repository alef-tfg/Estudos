"""
A ideia aqui é pegar o título de todos os inputus antes de clicarmos em qualquer coisa e quando clicarmos em cada um dos inputs e no submit
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver)

def print_titles(webdriver):
    titles = webdriver.find_elements(By.CSS_SELECTOR, 'div.form-group > label')
    for title in titles:
        print(title.text)
    print('\n')

class Escuta(AbstractEventListener):
    def before_click(self, elemento, webdriver):
        print(f'antes do click em {elemento.get_attribute("id")}')
        print_titles(webdriver)
        

    def after_click(self, elemento, webdriver):
        """
        Essa função cumpre o mesmo papel da before_click contudo quando clicamos no botão 
        somos direcionados para outra página e por isso o elemento não fica dispnível para
        que possamos pegar seu id depois do click por isso um erro ocorre e quando ele ocorrer
        a função irá continuar sem mostrar em qual elemento foi clicado
        """
        try:
            print(f'depois do click em {elemento.get_attribute("id")}')
        except:
            pass
        print_titles(webdriver) 


firefox = Firefox()

# montando o wrap do browser
wrapped_browser = EventFiringWebDriver(firefox, Escuta())

url = 'https://curso-python-selenium.netlify.app/exercicio_07'
wrapped_browser.get(url)

inputs = wrapped_browser.find_elements(By.CSS_SELECTOR, 'div.form-group > input')


inputs[0].click()
inputs[0].send_keys('Alef')

inputs[1].click()
inputs[1].send_keys('alef.tfg@gmail.com')

inputs[2].click()
inputs[2].send_keys('1234')

inputs[3].click()

