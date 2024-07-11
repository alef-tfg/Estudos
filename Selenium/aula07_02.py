from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver)

class Escuta(AbstractEventListener):
    def before_click(self, elemento, webdriver):
        print(f'antes do click no {elemento.tag_name}')
        if elemento.tag_name == 'input':
            print(webdriver.find_element(By.TAG_NAME, 'span').text)

    def after_click(self, elemento, webdriver):
        print(f'depois do click no {elemento.tag_name}')
        if elemento.tag_name == 'input':
            print(webdriver.find_element(By.TAG_NAME, 'span').text)



firefox = Firefox()

# montando o wrap do browser
wrapped_browser = EventFiringWebDriver(firefox, Escuta())

url = 'https://curso-python-selenium.netlify.app/aula_07_d'
firefox.get(url)

caixa_de_texto = wrapped_browser.find_element(By.TAG_NAME, 'input')
span = wrapped_browser.find_element(By.TAG_NAME, 'span')
p = wrapped_browser.find_element(By.TAG_NAME, 'p')

caixa_de_texto.click()
span.click()


firefox.quit()