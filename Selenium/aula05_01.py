from selenium.webdriver import Firefox

firefox = Firefox()

url = 'https://curso-python-selenium.netlify.app/aula_05_a.html'
firefox.get(url)

print(firefox.find_elements('tag name', 'h2'))