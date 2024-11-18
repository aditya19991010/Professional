
# credit: Introducing Python Book,
# https://medium.com/@nitin.data1997/web-scraping-imdb-data-with-python-and-beautifulsoup-f1d69812d3b

import urllib.request as ur
from urllib.parse import quote
import json
from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup
import csv
import html5lib

#sudo apt update
#sudo apt install apache2

def main():
   ### using urllib.request
   my_url = "http://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=1950,2012"
   uClient = uReq(my_url)
   page_html = uClient.read()
   uClient.close()
   # print(page_html)
   # parse html using beautifulsoup
   page_soup = BeautifulSoup(page_html, "html.parser")
   # print(page_soup.prettify())

   ### using requests - scrape a website
   URL = "http://www.values.com/inspirational-quotes"
   r = requests.get(URL)

   soup = BeautifulSoup(r.content, 'html5lib')

   quotes = []  # a list to store quotes

   table = soup.find('div', attrs={'id': 'all_quotes'})

   for row in table.findAll('div', attrs={'class': 'col-6'}):
      quote = {}
      quote['theme'] = row.h5.text
      quote['url'] = row.a['href']
      quote['img'] = row.img['src']
      quote['lines'] = row.img['alt'].split(" #")[0]
      quote['author'] = row.img['alt'].split(" #")[1]
      quotes.append(quote)

   filename = 'inspirational_quotes.csv'
   with open(filename, 'w', newline='') as f:
      w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
      w.writeheader()
      for quote in quotes:
         w.writerow(quote)

   print('End')




# Construct to not include whole program in other includes
if __name__ == "__main__":
   main()

