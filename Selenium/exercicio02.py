from selenium.webdriver import Firefox, FirefoxOptions
from time import sleep 
from pprint import pprint

navegador = Firefox()

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
navegador.get(url)
sleep(1)

ps = navegador.find_elements('tag name', 'p')
numero_esperado = int(ps[-1].text[16:])
print(f'O numero esperado é: {numero_esperado}')

a = navegador.find_element('tag name', 'a')
numero_atual = 0
while numero_esperado!=numero_atual:
    print(numero_atual!=numero_esperado, numero_esperado, numero_atual)
    a.click()
    sleep(1)
    ps = navegador.find_elements('tag name', 'p')
    try:
        numero_atual = int(ps[-1].text)
    except:
        numero_atual = int(ps[-1].text[13:])
        print('O número foi encontrado!')
input('press enter to end...')
navegador.quit()