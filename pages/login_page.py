from common.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage(BasePage):
    input_id = (By.ID, 'kw')
    # click_id = (By.ID, 'su')
    click_id = (By.XPATH, '//*[@id="su"]')

    def input_text(self, input_text):
        self.locator(self.input_id).send_keys(input_text)

    def click_element(self):
        self.locator(self.click_id).click()


if __name__ == '__main__':
    # url = 'http://www.baidu.com'
    url = 'https://www.12306.cn/index/'
    driver = webdriver.Chrome()
    sp = LoginPage(driver, url)
    # sp.input_text("哈哈哈")
    # sp.click_element()
    print(lambda x: x.find_element_by_id('toStation'))
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('toStation'))
