import bs4      # handle parsing
import requests # handle downloading

'''
Lets scrapping price info on amazon page
'''

res  =  requests.get('https://www.ebay.com/itm/No-Game-No-Life-Book-1-English-Manga-Yuu-Kamiya/253528884491')

res.raise_for_status()

#return a BeautifulSoup Object
soup = bs4.BeautifulSoup(res.text, 'html.parser')
#find html elements
elements = soup.select('#prcIsum')

# print(elements)

price = elements[0].text.strip

print(price)
