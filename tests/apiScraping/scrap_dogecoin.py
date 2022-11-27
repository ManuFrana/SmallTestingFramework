import requests
from bs4 import BeautifulSoup

"""
DuckDuckGo appears to be removed. Whenever i tried to fetch a response from https://api.duckduckgo.com
We get a "301 Moved Permanently" response
So i tried to fetch data directly from https://duckduckgo.com but they block data scraping by hashing the request
I tried to modify my user agent, but i was unsuccessfully
I provide an easy way to fetch links from another url.
THAT IS WHY I DECIDED TO SCRAP WHAT YOU ASK ME BY USING SELENIUM :)   (can be found in "scrap_with_selenium.py")
"""


# Url that we are going to use
url = "https://www.speedtest.net/es"

payload = {}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
# Get the response from the server
response = requests.request("GET", url, headers=headers, data=payload)
# Initialize BeautifulSoup to work with the html file
soup = BeautifulSoup(response.text, "html.parser")

links_found = []
# Iterate through every <a> ... </a> html element
for links in soup.find_all('a'):
    # Remove the unnecessary backslashes
    found = links.get('href').replace("\\", "")
    # Remove local links within the page
    if found.startswith('http') or found.startswith('www.'):
        links_found.append(found)


print("Welcome to dogeCoin scrapping")
if len(links_found) != 0:
    print("\nThese are the links that were found")
    print(links_found)
else:
    print("\nI did not find any links :(")
