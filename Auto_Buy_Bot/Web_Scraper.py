import requests
from bs4 import BeautifulSoup
from lxml import etree

def get_itemPrice(url, xpath_code):
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})

    re = requests.get(url, headers=HEADERS)
    res = re.content

    soup = BeautifulSoup(res, 'html.parser')

    dom = etree.HTML(str(soup))
    xpath = xpath_code
    price = dom.xpath(xpath)[0].text
    new_price = int(''.join([i for i in price if i != ',']))
    
    return new_price


#print(get_book_price('https://www.amazon.co.uk/Samsung-Odyssey-LC49G95TSSRXXU-Curved-Monitor/dp/B08WXGK8S1/ref=sr_1_1?crid=3OALESM5JT7LW&keywords=g9+odyssey&qid=1673973583&sprefix=g9+odyssey%2Caps%2C95&sr=8-1', '//*[@id="corePrice_feature_div"]/div/div/span/span[2]/span[2]'))