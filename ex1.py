from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://tvroom.github.io/selenium-exercises/ex1/")
elem = driver.find_element_by_css_selector('h3.sel_header')

assert "Selenium Test Header" in elem.text
print elem
driver.close()
