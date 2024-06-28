from selenium.webdriver import Firefox

browser = Firefox()
browser.get()
browser.current_url()

"""
from urllib.parse import urlparse
urlparse(browser.current_url) 
browser.refresh()
browser.title
"""