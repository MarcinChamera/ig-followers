from selenium import webdriver
from time import sleep
import platform

class InstaBot:
    # start up webdriver
    def __init__(self):
        if platform.system() == 'Linux':
            path_to_chromedriver = '/chromedriver/chromedriver'
        elif platform.system() == 'Windows':
            path_to_chromedriver = '/chromedriver/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=path_to_chromedriver)
        # chrome_options = webdriver.ChromeOptions()

        # # don't know if necessary on heroku
        # chrome_options.add_argument("--no-sandbox")

        # chrome_options.binary_location = '/app/.apt/usr/bin/google-chrome'
        # self.driver = webdriver.Chrome(executable_path='/app/.chromedriver/bin/chromedriver', chrome_options=chrome_options)       

    def login(self, username, password):
        self.driver.get("https://instagram.com")
        sleep(2)
        self.username = username
        sleep(1)
        # full xpath copied from inspect an element in chrome browser
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/p/a").click()
        sleep(1)
        # different way to get element
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").\
            send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").\
            send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").\
            click()
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")\
            .click()
        sleep(2)

    def get_unfollowers(self):
        #go to our profile (by finding <a> tag which contains href with our username)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        return not_following_back

    #placing underscore before private method's name is just a convention
    def _get_names(self):
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        #scroll to the bottom to load all names
        last_height, height = 0, 1
        while last_height != height:
            last_height = height
            sleep(0.5)
            #selenium enables using javascript
            height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names

    def logout(self):
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button/span")\
            .click()
        sleep(1)
        self.driver.find_elements_by_xpath("/html/body/div[4]/div/div/div/button[9]")
        sleep(3)

    def quit(self):
        self.driver.quit()
