__author__ = 'Joseph'


from selenium import webdriver
import unittest
import TestSuite
import random
import string
import  time

class ChromeTests(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path=r"C:\\Users\\Joseph\\Driver\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://hub.docker.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.userNameLogin = 'jarlia'
        self.passwordLogin = 'test123'
        self.email = self.userNameLogin+'@yahoo.com'
        self.signUpUname = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        self.signUpPassword =  ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        self.signUpEmail = self.signUpUname+'@yahoo.com'


    def test_01checkMainPage(self):
        driver = self.driver
        driver.get(self.base_url)
        main_banner = driver.find_element_by_xpath('/html/body/div/main/div[2]/div[2]/div/p').text
        self.assertEqual(main_banner[1:],' 2016 Docker Inc.','Home Page Test was successful')




    def test_02signUP(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/header/div/div[2]/div/form/div[1]/div/input").send_keys(self.signUpUname)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/header/div/div[2]/div/form/div[2]/div/input").send_keys(self.signUpEmail)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/header/div/div[2]/div/form/div[3]/div/input").send_keys(self.signUpPassword)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/header/div/div[2]/div/form/div[4]/button").click()
        time.sleep(5)
        verify_signup=driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/header/div/div[2]/div/div").text
        self.assertEqual(verify_signup,"Sweet! You're almost ready to go!","Sign up test complete")





    def test_03Login(self):
        driver = self.driver
        driver.get(self.base_url)
        uname = self.userNameLogin
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/nav/section/ul[3]/li[2]/a").click()
        driver.find_element_by_xpath("/html/body/div[1]/main/div/header/div[2]/div/form/div[1]/input").send_keys(self.userNameLogin)
        driver.find_element_by_xpath("/html/body/div[1]/main/div/header/div[2]/div/form/div[2]/input").send_keys(self.passwordLogin)
        driver.find_element_by_xpath("/html/body/div[1]/main/div/header/div[2]/div/form/div[3]/button").click()
        time.sleep(5)
        act_uName = driver.find_element_by_xpath('/html/body/div/main/div[1]/nav/section/ul[3]/li[3]/a/span/span').text
        act_uName = str(act_uName)
        self.assertEqual(uname,act_uName,'Test Passed: Expected User Name'+self.userNameLogin+' is equal to acutal user name '+act_uName+'')



    def test_04FailLogin(self):

        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/nav/section/ul[3]/li[2]/a").click()
        driver.find_element_by_xpath("/html/body/div[1]/main/div/header/div[2]/div/form/div[1]/input").send_keys(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))
        driver.find_element_by_xpath("/html/body/div[1]/main/div/header/div[2]/div/form/div[2]/input").send_keys(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))
        driver.find_element_by_xpath("/html/body/div[1]/main/div/header/div[2]/div/form/div[3]/button").click()
        time.sleep(5)
        self.assertRaises(Exception,lambda:driver.find_element_by_xpath('/html/body/div/main/div[1]/nav/section/ul[3]/li[3]/a/span/span').text)





    def test_05SearchRepository(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/nav/section/ul[3]/li[2]/a").click()
        driver.find_element_by_xpath("/html/body/div[1]/main/div/header/div[2]/div/form/div[1]/input").send_keys(self.userNameLogin)
        driver.find_element_by_xpath("/html/body/div[1]/main/div/header/div[2]/div/form/div[2]/input").send_keys(self.passwordLogin)
        driver.find_element_by_xpath("/html/body/div[1]/main/div/header/div[2]/div/form/div[3]/button").click()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/nav/section/ul[3]/li[1]/div/form/div/input').send_keys("test")
        driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/nav/section/ul[3]/li[1]/div/form/div/input').submit()
  #      repo_elem = driver.find_element(By.ID,".10bpk7wtce8.1.0.0.0.0").text
   #     repo_count = str(repo_elem).split("(")[1].split(")")[0]
    #    self.assertNotEqual(0,repo_count)




    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)





if __name__ == "__main__":


    Tests = TestSuite.TestSuite(ChromeTests)
    suite_preLogin = Tests.createPreLoginSuite()
    suite_postLogin = Tests.createPostLoginSuite()

    all_testSuite = unittest.TestLoader().loadTestsFromTestCase(ChromeTests)
    unittest.TextTestRunner(verbosity=2).run(all_testSuite)

