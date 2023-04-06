from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
action=ActionChains(driver)
time.sleep(10)
driver.implicitly_wait(10)
chat=driver.find_element_by_css_selector('span[title="XD"]')
action.click(chat).perform()
driver.implicitly_wait(5)
cursor=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
action.click(cursor).perform()
for x in range(50):
    cursor.send_keys("<3")
    cursor.send_keys(Keys.RETURN)
