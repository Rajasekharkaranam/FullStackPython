#Example Code
import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("Page Title:", soup.title.text)

for heading in soup.find_all("h1"):
    print("Heading:", heading.text)
#Extract Links
import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all("a"):
    print(link.get("href"))