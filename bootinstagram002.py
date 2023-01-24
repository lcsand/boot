from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\Lucas\PycharmProjects\untitled\Boot_Instagram\webdriver\geckodriver.exe')
        self.driver.get('https://www.instagram.com/accounts/emailsignup/')
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Conecte-se')]") \
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(password)
        sleep(2)
        self.driver.find_element_by_xpath("//button[@type='submit']") \
            .click()
        sleep(8)
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]") \
                .click()
        except:
            sleep(1)


    def get_unfollowers(self, username):
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), '{}')]".format(username)) \
            .click()
        sleep(5)
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]") \
            .click()
        sleep(2)
        following = self.get_names()
        print(len(following))
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]") \
            .click()
        sleep(2)
        followers = self.get_names()
        print(len(followers))
        sleep(2)
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
        print(len(not_following_back))

    def get_names(self):
        sleep(5)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        link = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in link if name != '']
        print(names)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names


        
    def get_following(self, *names):
        n = 0
        for name in names:
            try:
                sleep(1)
                n += 1
                self.driver.get('https://www.instagram.com/' +name+ '/')
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')\
                    .click()
            except:
                sleep(1)
        print(f'Seguindo {n} novos perfis')

    def notifications(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]/a/svg')\
            .click()

    def get_foloowing_based(self, *contacts):
        n = 0
        for contact in contacts:
            self.driver.get('https://www.instagram.com/' +contact+ '/')
            self.driver.find_element_by_xpath("//a[contains(@href, '/following')]") \
                .click()
            f_contact = self.get_names()

#//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button
#//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button
my_bot = InstaBot('pequenovinileiro', 'roll123-')
#my_bot.get_foloowing_based('pequenovinileiro')
my_bot.get_unfollowers('pequenovinileiro')
#my_bot.like_hashtag('vitrola')
#my_bot.get_following('letiandrade01', 'djregis.garcia')
#'vinil', 'discodevinil', 'disco', 'lp', 'longplay', 'vinyl', 'vinilo', 'vinile', 'vinylrecords','vinylcollection', 'vinilsp', 'vinylove', 'vinylclub', 'colecionadoresdevinil', 'vinilbrasil', 'vinylgram','instavinil', 'tocadisco', 'tocadiscos',