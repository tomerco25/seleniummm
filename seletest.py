from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
from config import *
import time

class runselenuim():
    global driver
    driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
    def __init__(self,passurl):
        self.passurl=passurl
    def usepass(self):
        driver.get(self.passurl)
        driver.maximize_window()
        #search = driver.find_element_by_xpath("//div[@id='signinDX']//form[@id='formx']//label[@id='luno']")
        search = driver.find_element_by_xpath("//input[starts-with(@id,'suno')]")
        search.send_keys('aaaaaaaaaa')
        search = driver.find_element_by_xpath("//input[@class='keyboardInput']")
        driver.find_element_by_xpath("//input[contains(@type,'pass')]").send_keys('passsssssssssssss')
        driver.find_element_by_xpath("//input[@class='keyboardInput' and @tabindex='2']").send_keys('199')
        search.send_keys('aaaaaaaaaa')


if __name__ == '__main__':
    runsel=runselenuim(passurl)
    runsel.usepass()
    time.sleep(2)
    driver.close()