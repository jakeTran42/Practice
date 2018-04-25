import bs4, requests

'''
Practice for WebScrapping for ebay price
'''

def getEbayPrice(URL):
    res = requests.get(URL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elements = soup.select('#prcIsum')
    elementTitle = soup.select('#itemTitle')

    # title = (elementTitle[0].text.strip().split('  '))[1] # This is one solution because there is a 'Detail Item' string attached to it
    title = (elementTitle[0].text.strip())[16:]             # This is a more simple solution because we know how many char is the trailing characters
    price = elements[0].text.strip()
    # print(title)

    return title, price

URList = [
'https://www.ebay.com/itm/No-Game-No-Life-Book-1-English-Manga-Yuu-Kamiya/253528884491',
'https://www.ebay.com/itm/Anime-Boku-no-hero-academia-My-Hero-Academia-Wall-Scroll-Poster-cosplay-2930/122660370997?_trkparms=aid%3D222007%26algo%3DSIM.MBE%26ao%3D2%26asc%3D44040%26meid%3D5e062309740943169d5a636373a8177a%26pid%3D100623%26rk%3D3%26rkt%3D6%26sd%3D253528884491%26itm%3D122660370997&_trksid=p2047675.c100623.m-1',
'https://www.ebay.com/itm/Anime-My-Boku-no-Hero-Academia-wall-Poster-Scroll-Cosplay-s3182/112583753657?_trkparms=aid%3D555018%26algo%3DPL.SIM%26ao%3D2%26asc%3D44040%26meid%3D640e9b202dc74b1ab2d41d4a37449a64%26pid%3D100005%26rk%3D1%26rkt%3D6%26sd%3D122660370997%26itm%3D112583753657&_trksid=p2047675.c100005.m1851',
'https://www.ebay.com/itm/The-Pet-Girl-Of-Sakurasou-Dakimakura-Mashiro-Shiina-Anime-Body-Pillowcase-Cover/291943645330?hash=item43f9328092:g:JV4AAOSwux5YKy7Z'
]

for item in URList:
    thisItem = getEbayPrice(item)
    print('The Item %s cost %s' % (thisItem[0], thisItem[1]))
