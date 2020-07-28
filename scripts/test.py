import random
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_helper import WebDriverHelper

search_string = []
s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie",
           "This cool guy my gardener met yesterday", "the Superman", "the Flash", "the Wonder-woman", "the Cat-woman"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats",
           "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people",
           "Supermen", "The Avengers"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards",
           "meows on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on",
           "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.",
               "to be able to make toast explode.", "to know more about archeology."]


def sentence_maker():
    # Makes a random sentence from the different parts of speech. Uses a SINGULAR subject'''
    try:
        return str(random.choice(s_nouns) + str(' ') + random.choice(s_verbs) + str(' ') + (
                random.choice(s_nouns).lower() or random.choice(p_nouns).lower()) + str(' ') + random.choice(
            infinitives))
    except Exception as e:
        print(f"Exception in sentence maker in browse_google :{e}")


def sdaads():
    for i in range(2):
        search_string.append(str(sentence_maker()).replace(' ', '+'))
    web_driver_helper = WebDriverHelper()
    if web_driver_helper.check_valid_driver_connection():
        web_driver_helper.driver = web_driver_helper.__enter__()
        string123 = "https://www.google.com/search?q=" + search_string[0] + "&start=" + str(0)
        matched_elements = web_driver_helper.driver.get(string123)
        print(web_driver_helper.driver.title)
        print(web_driver_helper.driver.current_url)
        print("Before Tab")
        main_window=web_driver_helper.driver.current_window_handle
        string1232 = "https://www.google.com/search?q=" + search_string[1] + "&start=" + str(1)
        web_driver_helper.driver.get(string1232)
        web_driver_helper.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+Keys.RETURN)
        web_driver_helper.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+ Keys.TAB)
        web_driver_helper.driver.switch_to.window(main_window)
        time.sleep(8)
        #ActionChains(web_driver_helper.driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
        web_driver_helper.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        web_driver_helper.driver.switch_to.window(main_window)
        print("After Tab")
        time.sleep(10)

sdaads()
