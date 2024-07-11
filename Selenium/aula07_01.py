from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

firefox = Firefox()

url = 'https://curso-python-selenium.netlify.app/aula_07_d'
firefox.get(url)

caixa_de_texto = firefox.find_element(By.TAG_NAME, 'input')
span = firefox.find_element(By.TAG_NAME, 'span')
p = firefox.find_element(By.TAG_NAME, 'p')

"""
Bloco de teste para verificar o evento de foco do input
"""
caixa_de_texto.click()
assert span.text == 'está com foco'
p.click()
assert span.text == 'está sem foco'

"""
Bloco teste para enviar string ao input e verificar o evento 
"""
assert p.text == '0', 'p não é zero'
caixa_de_texto.send_keys('batata')
assert span.text == 'está com foco', 'não está em foco'
span.click()
assert span.text == 'está sem foco', 'está em foco'
assert p.text == '1', 'p não é um'


firefox.quit()