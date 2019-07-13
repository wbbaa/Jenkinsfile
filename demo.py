# coding =utf-8

import requests,time
from selenium import webdriver
driver = webdriver.Chrome()

url='https://ec-demo.casstime.com/passport/login'
header={
    "Referer":"https://ec-demo.casstime.com/passport/login",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
def login():
  driver.get(url)
  driver.maximize_window()#将浏览器最大化
  driver.find_element_by_id("userName").send_keys("43241fz")
  driver.find_element_by_id("password").send_keys("123456")
  driver.find_element_by_xpath("//input[@value='登录']").click()
  
def inquery():
  #询价
  login()
  time.sleep(5)
  driver.find_element_by_id("guide-agentBuy").click()
  time.sleep(3)
  driver.find_element_by_id("vin").send_keys('sb66666')
  time.sleep(3)
  driver.find_element_by_xpath("//tr[@index='0']/td[@class='need-input-td']/div/textarea[@name='needName']").click()
  driver.find_element_by_xpath("//tr[@index='0']/td[@class='need-input-td']/div/textarea[@name='needName']").send_keys('火花塞')
  driver.find_element_by_xpath("//input[@value='NO']/preceding-sibling::i[@class='icon-new']").click()
  driver.find_element_by_xpath("//input[@value='发布询价']").click()
  
inquery()
  
