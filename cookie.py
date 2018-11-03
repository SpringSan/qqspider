# -*- coding: utf-8 -*-
# @Time    : 18-11-3 下午8:10
# @Author  : chunquansang
# @FileName: cookie.py
# @Software: PyCharm

from qqspier import config
from selenium import webdriver
from time import sleep
import json

driver = webdriver.Chrome()
driver.get('https://user.qzone.qq.com/{}/main'.format(config.qq))
driver.switch_to_frame('login_frame')
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys(config.qq);
driver.find_element_by_id('p').send_keys(config.password)
driver.find_element_by_id('login_button').click()

sleep(1)
cookies = driver.get_cookies()
cookie_dic={}
for cookie in cookies:
    if 'name' in cookie and 'value' in cookie:
        cookie_dic[cookie['name']] = cookie['value']
    with open('cookie_dic.txt', 'w') as f:
        json.dump(cookie_dic, f)


