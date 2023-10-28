#%%
import urllib.request #it is already available in python, I don't need to install it
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

page = urllib.request.urlopen('https://docs.python.org/3/library/random.html')
soup = bs(page)
print(soup)

soup.body.