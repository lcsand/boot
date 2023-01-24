from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'D:\Usuario\Desktop\bot_instagram\geckodriver.exe')


    def loguin(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/emailsignup/')
        sleep(5)
        loguin_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        loguin_button.click()
        sleep(5)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        sleep(5)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        sleep(5)
        password_element.send_keys(Keys.RETURN)
        sleep(20)
        self.curtir_fotos(hashtag)

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(5)
        hrefs = driver.find_elements_by_xpath("//a[contains(@href, '/p/')]")
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + 'fotos: ' + str(len(pic_hrefs)))
        for c in pic_hrefs:
            print(c)

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button/svg").click()
                print(pic_href)
                sleep(19)
            except Exception as e:
                sleep(5)
                print('erro')


#<svg aria-label="Curtir" class="_8-yf5 "
bot_ = InstagramBot('888888', '8888888')
bot_.loguin('python')
