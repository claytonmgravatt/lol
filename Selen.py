# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import sys
class Selen:

    def getPage(self, name) :
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        #chrome_options.add_argument("--disable-extensions")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        chrome_options.add_argument("--start-maximized")
        
        driver = webdriver.Chrome(executable_path=r'C:\Users\clayt\Desktop\Relevant\chromedriver_win32\chromedriver.exe', options = chrome_options)
        name = name.replace(' ','%20')
        driver.get('https://na.op.gg/summoner/userName=' + str(name))
        
        try :
            xpath = "(//*[@id='right_gametype_soloranked']/a)"
            ranked_button = driver.find_element_by_xpath(xpath)
            ranked_button.click()
            time.sleep(1)
            xpath2 = "(/html/body/div[8]/div/div[1]/svg)"
        except:
            print('Player '+str(name).replace('%20', ' ')+' not found! Please check spelling you fat retard')
            driver.quit()
            sys.exit()
        try:
            ad_button = driver.find_element_by_xpath(xpath2)
            ad_button.click()
        except:
            print('ad not loaded, good!')
        for x in range(0,5) :
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
            xpath1 = "(//*[@id='SummonerLayoutContent']/div[2]/div[2]/div/div[2]/div[" +str(4+x) + "]/a)"
            showMore_button = driver.find_element_by_xpath(xpath1)
            showMore_button.click()
            time.sleep(3)
            print(x)
        html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        driver.quit()
        return html

# doc = Selen.getPage(0, 'drf dive')
