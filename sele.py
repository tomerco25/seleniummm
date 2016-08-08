from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
from selenium.webdriver import *
from config import *
driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
class runselenuim():
    def __init__(self,wallaurl,passurl,bbcurl,checkboxurl):
        self.wallaurl=wallaurl
        self.passurl=passurl
        self.bbcurl=bbcurl
        self.checkboxurl=checkboxurl
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

    def bbc(self):
        driver.get(self.bbcurl)
        print driver.title
        search = driver.find_element_by_xpath("//div[@id='page']").text
        print search
        aa=driver.find_element_by_link_text("Republican splits grow over Trump")
        print aa
        aa.click()
    def checkbox(self):
        driver.get(self.checkboxurl)
        driver.implicitly_wait(0)
        driver.find_element_by_xpath("//input[@name='example2' and @type='radio']")

runsel=runselenuim(wallaurl,passurl,bbcurl,checkboxurl)
# runsel.usepass()
# runsel.walla()
#runsel.bbc()
runsel.checkbox()


