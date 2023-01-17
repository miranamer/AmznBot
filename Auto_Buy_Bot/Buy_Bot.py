from selenium import webdriver
import time
import twilio_keys

def BuyAmzn(url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("user-agent=Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; Build/KLP) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30")

    driver = webdriver.Chrome(options=options, executable_path="D:/Stuff/chromedriver_win32 (1)/chromedriver.exe")
    driver.get(url)

    skip_bttn = driver.find_element("xpath", "/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[2]/div/div[2]/a")
    skip_bttn.click()

    cookies = driver.find_element("xpath", '//*[@id="sp-cc-accept"]')
    cookies.click()

    buyNow = driver.find_element("xpath", '//*[@id="buy-now-button"]')
    buyNow.click()

    email = twilio_keys.email
    password = twilio_keys.password

    emailField = driver.find_element("xpath", '//*[@id="ap_email"]')
    emailField.send_keys(email)

    continueBttn = driver.find_element("xpath", '//*[@id="continue"]')
    continueBttn.click()


    passwordField = driver.find_element("xpath", '//*[@id="ap_password"]')
    passwordField.send_keys(password)


    continueBttn2 = driver.find_element("xpath", '//*[@id="signInSubmit"]')
    continueBttn2.click()

    driver.close()

    return True

#BuyAmzn("https://www.amazon.co.uk/Samsung-Odyssey-LC49G95TSSRXXU-Curved-Monitor/dp/B08WXGK8S1/ref=sr_1_1?crid=3OALESM5JT7LW&keywords=g9+odyssey&qid=1673973583&sprefix=g9+odyssey%2Caps%2C95&sr=8-1")
