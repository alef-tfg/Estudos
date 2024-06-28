# from selenium.webdriver import Chrome, ChromeOptions

# options = ChromeOptions()
# options.add_argument("--no-sandbox")

# navegador = Chrome(options=options)

from selenium.webdriver import Firefox

navegador = Firefox()

url = 'https://curso-python-selenium.netlify.app/aula_03.html'
navegador.get(url)

input('press enter to continue...')

navegador.quit()