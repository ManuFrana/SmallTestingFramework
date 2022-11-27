from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import warnings


class ScrapWithSelenium():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.wait = driverWait = WebDriverWait(self.driver, 8)

    def go(self, url):
        self.driver.get(url)

    def get_entire_page_html(self):
        return self.driver.page_source

    def get_page_images(self):
        all_images = self.driver.find_elements(By.XPATH, "//img[@src]")
        image_links = []
        for img in all_images:
            src_attribute = img.get_attribute("src")
            if not ((src_attribute.endswith('.ico') or (src_attribute.startswith('https://duckduckgo.com/')))):
                image_links.append(src_attribute)
        return image_links

    def show_links_in_html(self, html_file):
        soup = BeautifulSoup(html_file, "html.parser")
        links_found = []
        # Iterate through every <a> ... </a> html element
        for links in soup.find_all('a'):
            # Remove the unnecessary backslashes
            found = links.get('href')

            if (found is None):
                continue

            # Remove local links within the page
            if found.startswith('http') or found.startswith('www.'):
                links_found.append(found)

        print("\nWelcome to dogeCoin scrapping")
        if len(links_found) != 0:
            print("\nThese are the links that were found")
            return links_found
        else:
            print("\nI did not find any links :(")

    def close_driver(self):
        self.driver.close()


class DataResults():

    def __init__(self, data):
        self.data = data

    def show_results(self):
        for link in self.data:
            print(link)


warnings.filterwarnings("ignore", category=DeprecationWarning)
print("\nHello, Welcome to scrapping with selenium (DuckDuckGo api scrap did not work ;( )")
print("-------    MENU    -------")
print("1) Scrap DuckDuckGo with selenium and retrieve all images found when searching for  'dogs'")
print("2) Scrap DuckDuckGo with selenium and retrieve all links found when searching for 'dogecoin'")
print("3) Exit ;(")
opc = input("Select your option: ")
valids = ['1', '2', '3']
while opc not in valids:
    opc = input("Select correct your option: ")

if opc == '1':
    ###### DOG IMAGES WITH SELENIUM ######
    print("This is a list of all images found!")
    dogs = ScrapWithSelenium()
    dogs.go("https://duckduckgo.com/dogs")
    result_dogs = DataResults(dogs.get_page_images())
    result_dogs.show_results()
    dogs.close_driver()
elif opc == '2':
    ###### DOGCOIN LINSK WITH SELENIUM ######
    dogecoin = ScrapWithSelenium()
    dogecoin.go("https://duckduckgo.com/dogecoin")
    html_file = dogecoin.get_entire_page_html()
    print(dogecoin.show_links_in_html(html_file))
    dogecoin.close_driver()
else:
    print("BYEEEEE")


