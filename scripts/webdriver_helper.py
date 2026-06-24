from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverHelper:

    def __init__(self):
        self.driver = None
        # Use Service object for Selenium 4+ compatibility
        self.service = Service(ChromeDriverManager().install())
        
        # Suppress excessive USB/Bluetooth logging in terminal
        self.options = Options()
        self.options.add_argument("--disable-logging")
        self.options.add_argument("--log-level=3")

    def __enter__(self):
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.driver:
            self.driver.quit()

    """ PRIVATE """

    def check_valid_driver_connection(self):
        try:
            driver = webdriver.Chrome(service=self.service, options=self.options)
            print(f"[+] ChromeDriver successfully loaded: {driver.session_id}")
            driver.quit()
            return True
        except Exception as e:
            print(f"[-] Could not load ChromeDriver: {e}")
            return False

    def fetch(self, url):
        with self as d:
            d.get(url)