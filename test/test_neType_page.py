from selenium import webdriver
import unittest
from test.login import Login
from pages.neType_page import NeType

class NeTypeTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.url = 'http://10.2.12.48:18080'
        username = 'admin'
        password = 'Volte!2020'
        cls.lg = Login(cls.driver, cls.url)
        cls.lg.login(username, password)

    @classmethod
    def tearDownClass(cls) -> None:
        print("======================== Test End ========================")
        # cls.lg.quit_browser()

    def setUp(self) -> None:
        print("--------------------运行测试用例----------------")

    def tearDown(self) -> None:
        print("--------------------运行测试用例结束----------------")

    def test_add_neType(self):
        NeType(self.driver, self.url).add_neType()

if __name__ == '__main__':
    ts = unittest.TestSuite()
    ts.addTest(NeTypeTestCase("test_add_neType"))
    runner = unittest.TextTestRunner()
    runner.run(ts)