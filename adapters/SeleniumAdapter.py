# adapters/SeleniumAdapter.py
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from interfaces.WebDriverInterface import WebDriverInterface


class SeleniumAdapter(WebDriverInterface):
    def __init__(self):
        self.driver = webdriver.Chrome(self.chrome_options())

    def chrome_options(self):
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        return options

    def navigate_to_url(self, url):
        self.driver.get(url)

    def login(self, user):
        self.navigate_to_url("https://www.facebook.com/")
        email_field = self.find_element(By.XPATH, "//*[@id='email']")
        password_field = self.find_element(By.XPATH, "//*[@id='pass']")

        self.send_keys(email_field, user.username)
        time.sleep(random.randint(1, 3))
        self.send_keys(password_field, user.password)
        time.sleep(random.randint(1, 3))

        btn_login = self.find_element(
            By.XPATH, "//button[@data-testid='royal_login_button']")
        self.click(btn_login)
        print("Salut ", user.username, " vous etes connecte...")
        time.sleep(3)

    # Rechercher l'utilisateur sur Facebook
    def recherche(self, target_user):
        while True:
            try:
                search_field = self.find_element(
                    By.XPATH, "//input[@placeholder='Rechercher sur Facebook']")
                self.send_keys(search_field, target_user.username)
                time.sleep(3)
                # search_field.send_keys(Keys.DOWN)
                self.send_keys(search_field, Keys.ENTER)
                print("Recherche de ", target_user.username, " en cours...")
                time.sleep(5)
                btn_recherche = self.find_element(
                    By.XPATH, "//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1s688f xq9mrsl']")
                time.sleep(3)
                self.click(btn_recherche)
                print("On est bien sur la page de ",
                      target_user.username, "...")
                time.sleep(10)
                break
            except Exception as e:
                # print(f'{e}')
                self.navigate_to_url("https://www.facebook.com/")
                print("Actualisation...")
                continue

    def facebook_auto_liker(self, like_amount, scroll_speed):
        liked = 0
        tre = 0 
        i = -1 
        body_elem = self.driver.find_element(By.TAG_NAME, 'body')
        print("Je vais liker", like_amount, "photos.")
        while liked < like_amount:
            print("J’aime", liked, "/", like_amount)
            try:

                i += 1
                likes = self.driver.find_elements(By.XPATH,
                                                  "//div[@aria-label='J’aime']")
                try:
                    like_el = likes[i].find_elements(By.XPATH,
                                                     "a[contains(@aria-pressed, 'true')]")

                    if len(like_el) > 0:
                        print("Déjà aimé")
                    else:
                        likes[i].click()
                        liked += 1
                except Exception as e:
                    #print (e)
                    pass

                try:
                    discover_el = self.driver.find_elements(By.XPATH,
                                                            '//*[@id="appsNav"]/h4')
                except:
                    print("Impossible de localiser l'espace réservé du panneau gauche. Terminer.")
                    time.sleep(1)
                    break
                discover_el_location = discover_el[0].location
                location = likes[i].location
                body_elem.send_keys(Keys.DOWN)
                body_elem.send_keys(Keys.DOWN)

                body_elem = self.driver.find_element(By.TAG_NAME, 'body')
                while discover_el_location['y']+80 < location['y']:
                    if discover_el_location['y']+2000 < location['y']:
                        print(
                            "Les choses sont en panne, soit vous avez fait défiler vers le haut, soit la largeur de la fenêtre est trop petite. Terminer")
                        time.sleep(1)
                        return
                    discover_el = self.driver.find_elements(By.XPATH,
                                                            '//*[@id="appsNav"]/h4')
                    discover_el_location = discover_el[0].location
                    location = likes[i].location
                    size = likes[i].size
                    body_elem.send_keys(Keys.DOWN)
                    if location['y'] > 20000:
                        print("Feed too deep, refreshing")
                        self.driver.get("http://www.facebook.com")
                        n = random.randint(2, 11)
                        print("sleeping for ", n)
                        time.sleep(n)
                        i = -1

                    time.sleep(scroll_speed)

            except Exception as e:
                print(e)
                if tre < 3:
                    print("Rafraîchissant en.. :", 4-tre)
                    tre += 1
                    time.sleep(2)
                    body_elem = self.driver.find_element(By.TAG_NAME, 'body')
                    body_elem.send_keys(Keys.DOWN)
                    body_elem.send_keys(Keys.DOWN)
                    time.sleep(2)
                    body_elem.send_keys(Keys.DOWN)
                    body_elem.send_keys(Keys.DOWN)
                    time.sleep(2)

                else:

                    print("Les choses vont mal. rafraîchissant")
                    tre = 0
                    time.sleep(2)
                    i = 0
                    continue

    def find_element(self, locator, text):
        return self.driver.find_element(locator, text)

    def find_elements(self, locator, text):
        return self.driver.find_elements(locator, text)

    def click(self, element):
        element.click()

    def send_keys(self, element, text):
        element.send_keys(text)

    def quit(self):
        time.sleep(3)
        self.driver.quit()
