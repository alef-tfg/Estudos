"""
Usando event listner devemos resolver novamente o exercício 3
e devemos printar o after da navegação e o click para printar aonde a gente clica, o valor do que clicamos e printar sempre a
próxima aba no qual estamos navegando.
"""
from time import sleep
from pprint import pprint
from urllib.parse import urlparse
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver)

class Escuta(AbstractEventListener):
    def after_navigate_to(self, url, webdriver):
        print(url)
    
    def before_click(self, element, webdriver):
        print(f'a click is going to happen in the element that contains the following text: \"{element.text}\"')

    def after_click(self, element, webdriver):
        print(f'After clicking, we were redirected to {webdriver.current_url}')



firefox = Firefox()

# montando o wrap do browser
wrapped_browser = EventFiringWebDriver(firefox, Escuta())

url = 'https://curso-python-selenium.netlify.app/exercicio_03.html'
wrapped_browser.get(url)

sleep(0.5)

def find_element_by_text(wrapped_browser, tag, text):
    tags = wrapped_browser.find_elements('tag name', tag)
    for tag in tags:
        if tag.text == text:
            return tag


# Instruçõses para navegar na primeira página
main = wrapped_browser.find_element('tag name', 'main')
main_anchors = main.find_element('tag name', 'a')
main_anchors.click()

# Instruçõses para navegar na segunda página
main = wrapped_browser.find_element('tag name', 'main')
pergunta = main.find_elements('tag name', 'p')[1].text.split(' ')
muntiplication_result = str(int(pergunta[0]) * int(pergunta[2]))
anchors = main.find_elements('tag name', 'a')
[not_result := anchor.text for anchor in anchors if anchor.text != muntiplication_result]
find_element_by_text(wrapped_browser, 'a', str(not_result)).click()

# Instruçõses para navegar na terceir página
sleep(1)
titulo_pagina = wrapped_browser.title
find_element_by_text(wrapped_browser, 'a', str(titulo_pagina)).click()

# Instruçõses para navegar na quarta página
url_path = urlparse(wrapped_browser.current_url).path[1:]
sleep(1)
print(url_path)
find_element_by_text(wrapped_browser, 'a', str(url_path)).click()

# Instruçõses para navegar na quinta página
wrapped_browser.refresh()

input('press enter to end...')
wrapped_browser.quit()