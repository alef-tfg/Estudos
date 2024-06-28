from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

firefox = Firefox()

url = 'https://curso-python-selenium.netlify.app/exercicio_06.html'
firefox.get(url)

sleep(1)

def fill_form(navegador, form_class:str):
    """
    Fill out the form given it's class
    """
    form = navegador.find_element(By.CSS_SELECTOR, f'.form-{form_class}')
    print(form)

    form.find_element(By.CSS_SELECTOR, 'input[name="nome"]').send_keys('alef')
    form.find_element(By.CSS_SELECTOR, 'input[name="senha"]').send_keys('123')
    form.find_element(By.CSS_SELECTOR, f'input[name="{form_class}"]').click()

def find_form_to_fill():
    return firefox.find_element(By.CSS_SELECTOR, 'header span').text

while True:   
    form_name = find_form_to_fill()
    print(form_name)

    if form_name[0] != 'l' and form_name[2] != 'c':
        break

    fill_form(firefox, form_name)
    sleep(1)

