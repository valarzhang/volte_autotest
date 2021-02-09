from time import sleep
class BasePage(object):
    # 构造函数
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # 打开浏览器
    def open(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    # 元素定位
    def locator(self, locator):
        return self.driver.find_element(*locator)

    # 关闭
    def quit_browser(self):
        sleep(2)
        self.driver.quit()


