import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import xmlrunner

class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        cls.driver.get('file:///C:/Users/srdesai/VeativeWebVR/Structure_of_Phenol/login.html')
        cls.driver.implicitly_wait(10)
    
    def test_structure_of_phenol_girl(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get('file:///C:/Users/srdesai/VeativeWebVR/Structure_of_Phenol/login.html')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("username").send_keys("Radikha")
        self.driver.find_element_by_id("age").send_keys("25")
        element = Select(self.driver.find_element_by_name('gender'))
        element.select_by_value("Girl")
        element = Select(self.driver.find_element_by_name('avatar'))
        element.select_by_value("Monkey")
        self.driver.find_element_by_id("submitBtn").click()
        
    def test_structure_of_phenol_boy(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get('file:///C:/Users/srdesai/VeativeWebVR/Structure_of_Phenol/login.html')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("username").send_keys("Sanjeev Desai")
        self.driver.find_element_by_id("age").send_keys("25")
        element = Select(self.driver.find_element_by_name('gender'))
        element.select_by_value("Boy")
        element = Select(self.driver.find_element_by_name('avatar'))
        element.select_by_value("Monkey")
        self.driver.find_element_by_id("submitBtn").click()
        
    def test_avatar_monkey(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get('file:///C:/Users/srdesai/VeativeWebVR/Structure_of_Phenol/login.html')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("username").send_keys("Sanjeev Desai")
        self.driver.find_element_by_id("age").send_keys("25")
        element = Select(self.driver.find_element_by_name('gender'))
        element.select_by_value("Boy")
        element = Select(self.driver.find_element_by_name('avatar'))
        element.select_by_value("Monkey")
        self.driver.find_element_by_id("submitBtn").click()
    
    def test_avatar_snake(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get('file:///C:/Users/srdesai/VeativeWebVR/Structure_of_Phenol/login.html')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("username").send_keys("Sanjeev Desai")
        self.driver.find_element_by_id("age").send_keys("25")
        element = Select(self.driver.find_element_by_name('gender'))
        element.select_by_value("Boy")
        element = Select(self.driver.find_element_by_name('avatar'))
        element.select_by_value("Snake")
        self.driver.find_element_by_id("submitBtn").click()
        
    def test_Introduction_to_Complex_Numbers(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get('file:///C:/Users/srdesai/VeativeWebVR/Introduction_to_Complex_Numbers/login.html')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("username").send_keys("Sanjeev Desai")
        self.driver.find_element_by_id("age").send_keys("25")
        element = Select(self.driver.find_element_by_name('gender'))
        element.select_by_value("Boy")
        element = Select(self.driver.find_element_by_name('avatar'))
        element.select_by_value("Snake")
        self.driver.find_element_by_id("submitBtn").click()
        pass
    
    def test_Reproductive_Parts_of_a_Flower(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get('file:///C:/Users/srdesai/VeativeWebVR/Reproductive_Parts_of_a_Flower/login.html')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("username").send_keys("Sanjeev Desai")
        self.driver.find_element_by_id("age").send_keys("25")
        element = Select(self.driver.find_element_by_name('gender'))
        element.select_by_value("Boy")
        element = Select(self.driver.find_element_by_name('avatar'))
        element.select_by_value("Snake")
        self.driver.find_element_by_id("submitBtn").click()
        pass
    
    def test_Opaque_Translucent_and_Transparent(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get('file:///C:/Users/srdesai/VeativeWebVR/Opaque_Translucent_and_Transparent/login.html')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("username").send_keys("Sanjeev Desai")
        self.driver.find_element_by_id("age").send_keys("25")
        element = Select(self.driver.find_element_by_name('gender'))
        element.select_by_value("Boy")
        element = Select(self.driver.find_element_by_name('avatar'))
        element.select_by_value("Snake")
        self.driver.find_element_by_id("submitBtn").click()
        pass
    
    def test_Series_and_Parallel_Circuits(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get('file:///C:/Users/srdesai/VeativeWebVR/Series_and_Parallel_Circuits/login.html')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("username").send_keys("Sanjeev Desai")
        self.driver.find_element_by_id("age").send_keys("25")
        element = Select(self.driver.find_element_by_name('gender'))
        element.select_by_value("Boy")
        element = Select(self.driver.find_element_by_name('avatar'))
        element.select_by_value("Snake")
        self.driver.find_element_by_id("submitBtn").click()
        pass
    
    def test_Line_and_Plane_of_Symmetry(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get('file:///C:/Users/srdesai/VeativeWebVR/Line_and_Plane_of_Symmetry/login.html')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("username").send_keys("Sanjeev Desai")
        self.driver.find_element_by_id("age").send_keys("25")
        element = Select(self.driver.find_element_by_name('gender'))
        element.select_by_value("Boy")
        element = Select(self.driver.find_element_by_name('avatar'))
        element.select_by_value("Snake")
        self.driver.find_element_by_id("submitBtn").click()
        pass
    
    def test_lines(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get('file:///C:/Users/srdesai/VeativeWebVR/Lines/login.html')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("username").send_keys("Sanjeev Desai")
        self.driver.find_element_by_id("age").send_keys("25")
        element = Select(self.driver.find_element_by_name('gender'))
        element.select_by_value("Boy")
        element = Select(self.driver.find_element_by_name('avatar'))
        element.select_by_value("Snake")
        self.driver.find_element_by_id("submitBtn").click()
        pass
    
    def test_humun_brain(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get('file:///C:/Users/srdesai/VeativeWebVR/Human_Brain/login.html')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("username").send_keys("Sanjeev Desai")
        self.driver.find_element_by_id("age").send_keys("25")
        element = Select(self.driver.find_element_by_name('gender'))
        element.select_by_value("Boy")
        element = Select(self.driver.find_element_by_name('avatar'))
        element.select_by_value("Snake")
        self.driver.find_element_by_id("submitBtn").click()
        pass
    def test_login_form_validations(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get('http://ec2-52-5-117-32.compute-1.amazonaws.com/unicef/public/')
        self.driver.implicitly_wait(10)
        loginurl = '//a[contains(text(),\'Login\')]'
        username = '//input[@id=\'unicef_username\']'
        passwd = '//input[@id=\'unicef_password\']'
        loginbtn = '//input[@id=\'login-btn\']'
        loginelement = WebDriverWait(self.driver,10).until(lambda driver:self.driver.find_element_by_xpath(loginurl))
        loginelement.click()
        user_element = WebDriverWait(self.driver,10).until(lambda driver:self.driver.find_element_by_xpath(username))
        user_element.send_keys("sanjeev")
        passwd_element = WebDriverWait(self.driver,10).until(lambda driver:self.driver.find_element_by_xpath(passwd))
        passwd_element.send_keys("admin1234")
        btn_element = WebDriverWait(self.driver,10).until(lambda driver:self.driver.find_element_by_xpath(loginbtn))
        btn_element.click()
        print("logged in successfully")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed..!!")
        

            
if __name__ == "__main__":
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test_result'))