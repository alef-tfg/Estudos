from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver)

class Escuta(AbstractEventListener):
    def before_navigate_to(self, url, webdriver):
        print(f'Indo para {url}')
    
    def after_navigate_back(self, webdriver):
        print('voltando para a página anterior')


firefox = Firefox()

# montando o wrap do browser
wrapped_browser = EventFiringWebDriver(firefox, Escuta())

url = 'https://curso-python-selenium.netlify.app/aula_07_d'
wrapped_browser.get(url)

caixa_de_texto = wrapped_browser.find_element(By.TAG_NAME, 'input')
span = wrapped_browser.find_element(By.TAG_NAME, 'span')
p = wrapped_browser.find_element(By.TAG_NAME, 'p')

wrapped_browser.get(url[:-1]+'c')
sleep(3)
wrapped_browser.back()

firefox.quit()