from selenium.webdriver import Firefox, FirefoxOptions
from time import sleep 
from pprint import pprint

navegador = Firefox()

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
navegador.get(url)
sleep(1)

h1 = navegador.find_element('tag name','h1')
ps = navegador.find_elements('tag name', 'p')


content={p.get_attribute('atributo') : p.text for p in ps}
result = {'h1': content}
pprint(result)

input('press enter to continue...')

navegador.quit()