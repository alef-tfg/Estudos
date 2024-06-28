from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from time import sleep
from json import loads #formating json to python dict

firefox = Firefox()

url = 'https://curso-python-selenium.netlify.app/exercicio_04.html'
firefox.get(url)

sleep(1)

def preeecher_form(navegador, nome, email, senha, telefone):
    '''
    Preenche automarticamente o formulário da página
    '''
    navegador.find_element(By.NAME, 'nome').send_keys(nome)
    navegador.find_element(By.NAME, 'email').send_keys(email)
    navegador.find_element(By.NAME, 'senha').send_keys(senha)
    navegador.find_element(By.NAME, 'telefone').send_keys(telefone)
    input('press enter to finish...')
    navegador.find_element(By.ID, 'btn').click()

form_data = {'nome': 'alef', 
             'email': 'a@gmail.com', 
             'senha': 'hsuahusha', 
             'telefone': '85999999999'
             }

preeecher_form(firefox, **form_data)


result_string = firefox.find_element(By.TAG_NAME, 'textarea').text.replace('\'', '\"')

assert form_data == loads(result_string)