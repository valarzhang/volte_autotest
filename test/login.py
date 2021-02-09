from common.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Login(BasePage):
    # url = 'http://www.baidu.com'
    # dr = webdriver.Chrome()
    # dr.get(url)
    input_username = (By.XPATH, '//input[@placeholder="请输入用户名"]')
    input_password = (By.XPATH, '//input[@placeholder="请输入密码"]')
    input_code = (By.XPATH, '//input[@placeholder="请输入验证码"]')
    click_button = (By.TAG_NAME, 'button')

    # input_CITY = (By.NAME, '南京')
    # click_id = (By.XPATH, '//*[@id="su"]')

    def login(self, username, password):
        self.open()
        self.locator(self.input_username).send_keys(username)
        self.locator(self.input_password).send_keys(password)
        code = input("请输入验证码：")
        self.locator(self.input_code).send_keys(code)
        self.locator(self.click_button).click()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = ''
    sp = Login(driver, url)
    sp.login('南京', 123)
