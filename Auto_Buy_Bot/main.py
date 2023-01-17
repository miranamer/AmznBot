from Web_Scraper import get_itemPrice
from Buy_Bot import BuyAmzn
from Confirm_Bot import sendConfirmation

target_url = 'https://www.amazon.co.uk/Samsung-Odyssey-LC49G95TSSRXXU-Curved-Monitor/dp/B08WXGK8S1/ref=sr_1_1?crid=3OALESM5JT7LW&keywords=g9+odyssey&qid=1673973583&sprefix=g9+odyssey%2Caps%2C95&sr=8-1'
target_xpath = '//*[@id="corePrice_feature_div"]/div/div/span/span[2]/span[2]'

itemPrice = get_itemPrice(target_url, target_xpath)
targetPrice = 1500

print(itemPrice)

if itemPrice < targetPrice:
    BuyAmzn(target_url) # buy item
    sendConfirmation() # send sms

else:
    print('Price Is Too High')
