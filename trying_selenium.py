
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')
elem = browser.find_element_by_css_selector(
    '.main > div:nth-child(1) > div:nth-child(3) > a:nth-child(1)')
elem.try:

elem.click()

except expression as identifier:
    pass
