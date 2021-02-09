from selenium.webdriver.common.by import By
from common.base_page import BasePage
from time import sleep



class NeType(BasePage):
    basicConfig_menu = (By.XPATH, '//span[contains(text(), "基础配置")]')
    neType_menu = (By.XPATH, '//span[contains(text(), "网元字典")]')
    add_button = (By.XPATH, '//span[contains(text(), "新增")]')
    input_neType = (By.XPATH, '//input[@placeholder="输入网元类型"]')
    select_image = (By.XPATH, '//div[@class="ivu-form-item-content"]/img[1]')
    submit_button = (By.XPATH, '//span[contains(text(), "确定")]')

    def add_neType(self):
        self.locator(self.basicConfig_menu).click()
        self.locator(self.neType_menu).click()
        self.locator(self.add_button).click()
        self.locator(self.input_neType).send_keys('test0209')
        self.locator(self.select_image).click()
        self.locator(self.submit_button).click()




