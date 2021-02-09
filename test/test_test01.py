import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By

from test.login import Login
from time import sleep


@ddt
class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("======================== Test Start ========================")
        url = 'http://10.2.12.48:18080/#/login'
        # url = 'http://10.2.12.48:18080/#/home'
        driver = webdriver.Chrome()
        cls.lg = Login(driver, url)

    @classmethod
    def tearDownClass(cls) -> None:
        print("======================== Test End ========================")
        # cls.lg.quit_browser()

    def setUp(self) -> None:
        print("--------------------运行测试用例----------------")

    def tearDown(self) -> None:
        print("--------------------运行测试用例结束----------------")

    # @data(('admin', 'Volte!2020'), ('admin', ''), ('', 'Volte!2020'))
    @data(('admin', 'Volte!2020', (By.XPATH, '//span[contains(text(),"登录成功")]')))
    @unpack
    def test_01_login(self, username, password=None, element=None):
        self.lg.login(username, password)
        print(element)
        result = self.lg.locator(element)
        print(result)
        self.assertTrue(result)
        sleep(5)

    # def test_01_login(self):
    #     self.lg.login('admin', 'Volte!2020')


if __name__ == '__main__':
    ts = unittest.TestSuite()
    ts.addTest(LoginTestCase("test_01_login"))
    runner = unittest.TextTestRunner()
    runner.run(ts)
