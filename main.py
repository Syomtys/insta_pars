import requests
from bs4 import BeautifulSoup
import re

inp = input()

respown = requests.get(inp)
soup = BeautifulSoup(respown.content, 'html.parser')
print(soup)
