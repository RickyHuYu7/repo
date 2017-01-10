from selenium import webdriver
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
import sys


class GetFirstPage():

    def __init__(self, website):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(website)
		self.test = 2

    def GetHotStartContinent(self):
        startcityxpath = '//*[@id="bgList"]/div[1]/div[1]/div[3]/div/form/div/div[2]/div[1]/div[1]/label/input'
        self.driver.find_element_by_xpath(startcityxpath).click()
        n = 1
        x = 0
        n = str(n)
        time.sleep(1)
        #self.driver.find_element_by_xpath(continentlist).click()
        while self.driver.find_element_by_xpath(
                '//*[@id="bgList"]/div[1]/div[1]/div[3]/div/form'
                '/div/div[2]/div[1]/div[1]/label/div/div[1]/div[1]/ul/li[' + n + ']'):
            n = int(n)
            n += 1
            n = str(n)
            x += 1
            try:
                self.driver.find_element_by_xpath('//*[@id="bgList"]/div[1]/div[1]/div[3]/div/form'
                '/div/div[2]/div[1]/div[1]/label/div/div[1]/div[1]/ul/li[' + n + ']')
            except:
                break

        m = random.randint(1, x)
        m = str(m)
        print m
        getcontinent = self.driver.find_element_by_xpath('//*[@id="bgList"]/div[1]/div[1]/div[3]/div/form/div/div[2]'
                                         '/div[1]/div[1]/label/div/div[1]/div[1]/ul/li[' + m + ']/a')
        ActionChains(self.driver).move_to_element(getcontinent).perform()

    def GetHotStartCity(self):
        html = self.driver.find_elements_by_class_name("city-item")
        citylist = []
        for item in html:
            citylist.append(item.text)
        n = len(citylist)
        m = random.randint(1, n)
        print n, m
        self.driver.find_element_by_link_text(citylist[m]).click()

    def GetHotArriveContinent(self):
        startcityxpath = '//*[@id="bgList"]/div[1]/div[1]/div[3]/div/form/div/div[2]/div[1]/div[3]/label/input'
        self.driver.find_element_by_xpath(startcityxpath).click()
        n = 1
        x = 0
        n = str(n)
        time.sleep(1)
        #self.driver.find_element_by_xpath(continentlist).click()
        while self.driver.find_element_by_xpath(
                '//*[@id="bgList"]/div[1]/div[1]/div[3]/div/form/div/div[2]/div[1]'
                '/div[3]/label/div/div[1]/div[1]/ul/li[' + n + ']'):
            n = int(n)
            n += 1
            n = str(n)
            x += 1
            try:
                self.driver.find_element_by_xpath('//*[@id="bgList"]/div[1]/div[1]/div[3]/div/form'
                '/div/div[2]/div[1]/div[3]/label/div/div[1]/div[1]/ul/li[' + n + ']')
            except:
                break

        m = random.randint(1, x)
        m = str(m)
        print m
        getcontinent = self.driver.find_element_by_xpath('//*[@id="bgList"]/div[1]/div[1]/div[3]/div/form/div/div[2]'
                                         '/div[1]/div[3]/label/div/div[1]/div[1]/ul/li[' + m + ']/a')
        ActionChains(self.driver).move_to_element(getcontinent).perform()

    def GetStartDate(self):
        self.driver.find_element_by_xpath('//*[@id="bgList"]/div[1]/div[1]/div[3]/div/form/div'
                                          '/div[2]/div[2]/label/div/input').click()
        self.driver.find_element_by_xpath('//*[@id="bgList"]/div[1]/div[1]/div[3]/div/form/div/div[2]/'
                                          'div[2]/div/div[2]/div[2]/div[1]/div[3]/a[11]/b/i').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="bgList"]/div[1]/div[1]/div[3]/div/form/div/div[2]/'
                                          'div[2]/div/div[2]/div[2]/div[2]/div[3]/a[17]/b').click()


try:
    a = GetFirstPage('https://www.igola.com/')
    a.driver.implicitly_wait(20)
    a.GetHotStartContinent()
    time.sleep(1)
    a.GetHotStartCity()
    a.GetHotArriveContinent()
    time.sleep(1)
    a.GetHotStartCity()
    a.GetStartDate()
    a.driver.find_element_by_xpath('//*[@id="bgList"]/div[1]/div[1]/div[3]/div/form/div/div[2]/a[1]').click()
    a.driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[7]').click()

finally:
    time.sleep(20)
    a.driver.quit()
