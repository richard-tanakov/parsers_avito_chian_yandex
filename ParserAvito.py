
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from rich import print as print



def parse_avito(url : str):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument("--enable-javascript")
    options.add_argument('--headless')
    browser  =   webdriver.Chrome(options=options)

    browser.get(url)
    browser.add_cookie({"name": "foo", "value": "bar"})

    try:
        status   =  browser.find_element(By.CSS_SELECTOR,'.closed-warning-block-_5cSD').text
        price = browser.find_element(By.CSS_SELECTOR, '.style-item-price-main-jpt3x > span:nth-child(1) > span:nth-child(3) > span:nth-child(1)' ).text
        status = False
        return price, status
    except Exception as e:    
        try:
            status = 'Активно'
            price = browser.find_element(By.CSS_SELECTOR, '.style-item-price-main-jpt3x > span:nth-child(1) > span:nth-child(3) > span:nth-child(1)' ).text
            #adress = browser.find_element(By.CSS_SELECTOR, '.style-item-address__string-wt61A').text
            status = True
            return (price, status)
        except Exception as e:
            
                    status = False
                    price = 0
                    return price, status




