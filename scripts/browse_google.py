import time
import random
import numpy
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_helper import WebDriverHelper

past_url_1 = ["", "", ""]
past_url_2 = ["", "", ""]
depth = 0
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

"""
Function: Checks whether `url` is a valid URL.
Parameters: string 'URL'
Returns: if the url is valid or not
"""


def is_valid(url):
    try:
        parsed = urlparse(url)
    except Exception as e:
        print(f"Exception in is_valid in browse_google:{e}")
    return bool(parsed.netloc) and bool(parsed.scheme)


"""
Function: Returns all URLs that is found on `url` in which it belongs to the same website
Parameters:string 'url'
Returns: List of URLs
"""


def get_all_website_links(url):
    try:
        # all URLs of `url`
        urls = set()
        # domain name of the URL without the protocol
        domain_name = urlparse(url).netloc
        print(domain_name)
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                # if href is empty
                continue
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            # removing Get Parameters
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            if not is_valid(href):
                # not a valid url
                continue
            urls.add(str(href))
    except Exception as e:
        print(f"Exception in get_all_website_links in browse_google"
              f":{e}")
    return urls


"""
Function: Emulate browsing action
Parameters: driver: Web Driver
Returns:
"""


def tab_management(driver):
    pass


def browse(driver):
    try:
        global depth
        global past_url_1
        global past_url_2
        urls = get_all_website_links(driver.current_url)
        if depth < 3:
            past_url_1[depth] = driver.current_url
            if len(urls) > 4:
                driver.get(list(urls)[random.choice(range(4, len(urls) + 1))])
            else:
                driver.get(list(urls))[random.choice(range(len(urls)))]
            print(driver.title)
            print(driver.current_url)
            print("qweasdkjergtnljc ;ldsfk asjfklvsadfnascdlfikj maws cvjahe;wv  fweaif; ")
            depth += 1
            #if random.choice([True, False], p=[0.99, 0.01], replace=True):
            #tab_management(driver)
            browse(driver)
        else:
            print(depth)
            if depth != 0:
                depth -= 1
                depth = random.choice(range(len(past_url_1)))
                driver.get(past_url_1[depth])
                browse(driver)
            else:
                driver.close()
                return
    except Exception as e:
        print(f"Exception in browse in browse_google:{e}")


"""
Function:
Parameter:
Returns:
"""


def tab_management(driver):
    #print("qwertyyuiopasdfghjklzxcvbnm1234566788901qaz2")
    print(f"{driver.current_url}")
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
    driver.get("https://www.google.com/")
    print(f"{driver.current_url}")
    time.sleep(7)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
    time.sleep(10)
    print(f"{driver.current_url}")
    driver.switch_to.window(driver.window_handles[-1])
    pass


"""
Function:Generates a sentence   
Parameters:
Returns: returns a sentence
"""


def sentence_maker():
    # Makes a random sentence from the different parts of speech. Uses a SINGULAR subject'''
    try:
        return str(random.choice(s_nouns) + str(' ') + random.choice(s_verbs) + str(' ') + (
                random.choice(s_nouns).lower() or random.choice(p_nouns).lower()) + str(' ') + random.choice(
            infinitives))
    except Exception as e:
        print(f"Exception in sentence maker in browse_google :{e}")


"""
Function: Browse google (main function)
Parameters:
Returns:
"""


def google_browser():
    try:
        global depth
        search_string = []
        for i in range(2):
            search_string.append(str(sentence_maker()).replace(' ', '+'))
        web_driver_helper = WebDriverHelper()
        try:
            if web_driver_helper.check_valid_driver_connection():
                # print(f"Completed the driver check!{web_driver_helper.driver}")
                for i in range(len(search_string)):
                    web_driver_helper.driver = web_driver_helper.__enter__()
                    string123 = "https://www.google.com/search?q=" + search_string[i] + "&start=" + str(i)
                    matched_elements = web_driver_helper.driver.get(string123)
                    print(web_driver_helper.driver.title)
                    print(web_driver_helper.driver.current_url)
                    val = numpy.random.choice([True, False], replace=True, p=[0.3, 0.7])
                    if val:
                        # print("Inside the 'if'")
                        depth = 0
                        browse(web_driver_helper.driver)
                    else:
                        r = random.uniform(1, 10) or random.uniform(60, 100)
                        print(f"Sleep :{r}")
                        time.sleep(r)
        except Exception as e:
            print(f"Exception:{e}")
        web_driver_helper.driver.close()
    except Exception as e:
        print(f"Exception in google_browser: {e}")


google_browser()
