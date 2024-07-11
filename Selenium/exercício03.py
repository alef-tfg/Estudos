from selenium.webdriver import Firefox
from time import sleep 
from urllib.parse import urlparse

navegador = Firefox()
url = 'https://curso-python-selenium.netlify.app/exercicio_03.html'
navegador.get(url)
sleep(0.5)

def find_element_by_text(navegador, tag, text):
    tags = navegador.find_elements('tag name', tag)
    for tag in tags:
        print(tag.text, text)
        if tag.text == text:
            return tag


# Instruçõses para navegar na primeira página
main = navegador.find_element('tag name', 'main')
main_anchors = main.find_element('tag name', 'a')
navegador.get(main_anchors.get_attribute('href'))

# Instruçõses para navegar na segunda página
main = navegador.find_element('tag name', 'main')
pergunta = main.find_elements('tag name', 'p')[1].text.split(' ')
muntiplication_result = str(int(pergunta[0]) * int(pergunta[2]))
anchors = main.find_elements('tag name', 'a')
[not_result := anchor.text for anchor in anchors if anchor.text != muntiplication_result]
navegador.get(find_element_by_text(navegador, 'a', str(not_result)).get_attribute('href'))

# Instruçõses para navegar na terceir página
sleep(1)
titulo_pagina = navegador.title
navegador.get(find_element_by_text(navegador, 'a', str(titulo_pagina)).get_attribute('href'))

# Instruçõses para navegar na quarta página
url_path = urlparse(navegador.current_url).path[1:]
sleep(1)
print(url_path)
navegador.get(find_element_by_text(navegador, 'a', str(url_path)).get_attribute('href'))

# Instruçõses para navegar na quinta página
navegador.refresh()

input('press enter to end...')
navegador.quit()