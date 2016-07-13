from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
from config import *
driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
class runselenuim():
    def __init__(self,wallaurl,passurl):
        self.wallaurl=wallaurl
        self.passurl=passurl
    def usepass(self):
        driver.get(self.passurl)
        #search = driver.find_element_by_xpath("//div[@id='signinDX']//form[@id='formx']//label[@id='luno']")
        search = driver.find_element_by_xpath("//input[starts-with(@id,'suno')]")
        search.send_keys('aaaaaaaaaa')
        search = driver.find_element_by_xpath("//input[@class='keyboardInput']")
        driver.find_element_by_xpath("//input[contains(@type,'pass')]").send_keys('passsssssssssssss')
        driver.find_element_by_xpath("//input[@class='keyboardInput' and @tabindex='2']").send_keys('199')
        search.send_keys('aaaaaaaaaa')

    def walla(self):
        driver.get(self.wallaurl)
        try:
            search = driver.find_element_by_xpath("//a[@rel='nofollow']").click()
        except:
            search = driver.find_element_by_xpath("//aj[@rel='nofollow']").click()
        else:
            print "success"

runsel=runselenuim(wallaurl,passurl)
runsel.usepass()
runsel.walla()


