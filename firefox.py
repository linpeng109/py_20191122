# 在RaspberryPI上实现网页数据抓取
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

myItem = {
    'title': '',
    'content': '',
    'foot': ''
}

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
browser = webdriver.Firefox(options=options)
browser.implicitly_wait(30)
browser.get('http://www.baidu.com')
elem = browser.find_element_by_name('wd')
# elem.send_keys(sys.argv[1] + Keys.RETURN)
elem.send_keys('中矿智信' + Keys.RETURN)
# result = browser.find_elements_by_xpath('//div[contains(@class,"c-container")]')
xpath = '//div[contains(@class,"c-container")]'
# xpath = '//div[@id="wrapper"]/div[@id="wrapper_wrapper"]/div[@id="container"]/div[@id="content_left]/div[contains(@class,"c-container")]'
result = browser.find_elements_by_xpath(xpath=xpath)
for item in result:
    print(item.text)

browser.quit()
