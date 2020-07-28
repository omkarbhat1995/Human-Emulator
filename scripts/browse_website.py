import time
import random
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from webdriver_helper import WebDriverHelper

depth = 0
past_url_1 = ["", "", ""]
loops = 0
"""
Function: Checks whether `url` is a valid URL.
Parameters: string 'URL'
Returns: if the url is valid or not
"""


def is_valid(url):
    try:
        parsed = urlparse(url)
    except Exception as e:
        print(f"Exception in is_valid in browse_website:{e}")
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
        domain_name = urlparse(str(url)).netloc
        print(domain_name)
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                # if href is empty
                continue
            href = urljoin(str(url), href)
            parsed_href = urlparse(href)
            # removing Get Parameters
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            if not is_valid(str(href)):
                # not a valid url
                continue
            urls.add(str(href))
    except Exception as e:
        print(f"Exception in get_all_website_links in browse_website:{e}")
    return urls


"""
Function: Emulate browsing action
Parameters: driver: Web Driver ; website: List of websites.
Returns:
"""


def browse(driver, website):
    try:
        global depth
        global loops
        # depth += 1
        urls = get_all_website_links(driver.current_url)
        if depth < 3:
            past_url_1[depth] = driver.current_url
            if len(urls) > 4:
                driver.get(list(urls)[random.choice(range(4, len(urls)))])
            else:
                driver.get(list(urls))[random.choice(range(len(urls)))]
            print(driver.title)
            print(driver.current_url)
            depth += 1
            time.sleep(random.choice(range(21)))
            browse(driver, website)
        else:
            # print(depth)
            if depth != 0:
                depth -= 1
                loops += 1
                depth = random.choice(range(len(past_url_1)))
                driver.get(past_url_1[depth])
                browse(driver, website)
            elif loops > 30:
                driver.close()
                return
            else:
                driver.close()
                return
    except Exception as e:
        print(f"Exception in browse in browse_website:{e}")


"""
Function: Processes Data
Parameters: filename: Name of the file with list of websites.
Returns: List of websites
"""


def process_data(filename):
    try:
        websites = []
        with open(filename, 'r') as f:
            for line in f:
                websites.append(str(line).replace('\n', ''))
        return websites
    except Exception as e:
        print(f"Exception in process_data in browse_website:{e}")


"""
Function: Browse websites (main function)
Parameters:
Returns:
"""


def website_browser():
    try:
        print("Website Browser")
        web_driver_helper = WebDriverHelper()
        websites = process_data('data/websites.txt')
        if web_driver_helper.check_valid_driver_connection():
            driver = web_driver_helper.__enter__()
            name = 'https://' + str(random.choice(websites))
            print(name)
            driver.get(name)
            browse(driver=driver, website=websites)
    except Exception as e:
        print(f"Exception in browse_website:{e}")


website_browser()
