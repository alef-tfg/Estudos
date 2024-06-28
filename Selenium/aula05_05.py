from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

firefox = Firefox()

url = 'https://curso-python-selenium.netlify.app/aula_05.html'
firefox.get(url)

firefox.find_elements('name')

#nome email senha telefone, btn
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

preeecher_form(firefox, 'alef', 'a@gmail.com', 'kkkkk', '85999999999')

