from selenium import webdriver
from time import sleep

# name和value值来源，
#     1、在登录页面点击F12，点击Application目录，然后会看到Cookies，点击Cookies下的链接，并且清空里面的值。
#     2、输入账号密码登录，登录成功之后，Cookies会有登录后的Cookies值，将该值填写到代码中即可。
#

driver = webdriver.Chrome()
driver.get('http://10.2.12.48:18080/#/kpi-design')  # 登录页面路径

