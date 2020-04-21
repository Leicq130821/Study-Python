from selenium import webdriver
import unittest
class Test(unittest.TestCase):
    # 通过self.browser将webdriver.Ie()变成全局属性绑定在实例化对象上，其他方法既可以直接进行使用。
    def setUp(self):
        self.browser=webdriver.Ie()
        browser=self.browser
        browser.maximize_window()
        browser.implicitly_wait(5)
        browser.get('https://www.baidu.com')
    def test1(self):
        browser=self.browser
        browser.find_element_by_id('kw').send_keys('python')
        browser.find_element_by_id('su').click()
    def test2(self):
        browser = self.browser
        browser.find_element_by_id('kw').send_keys('自动化测试')
        browser.find_element_by_id('su').click()
    def tearDown(self):
        browser=self.browser
        browser.quit()
if __name__=='__main__':
    unittest.main()