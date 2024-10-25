
import requests
from bs4 import BeautifulSoup 
from rich import print
from time import sleep
import random
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from rich import print as print
import logging



logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a")


options = ChromeOptions()


class ParserCian:
    def get_url(url):
        headers  =   {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
        sleep_time = random.uniform(10, 100)
        sleep(sleep_time)
        response    =   requests.get(url=url, headers=headers)
        
        
        if response.status_code == 404:
        
                print("Объявление удалено", url)
        
        
        logging.info(f'Статус запроса Циан {url}, {response.status_code}')
        return response,url 
        



    def html_chian_content(response,url):
            """ Получение контента """            
            soup     =      BeautifulSoup(response.content, 'html.parser')

            price    =      soup.select('.a10a3f92e9--amount--ON6i1 > span:nth-child(1)')[0].get_text().replace('\xa0','')

            info  =      soup.select('.a10a3f92e9--address-line--GRDTb > div:nth-child(1)')[0].get_text().replace('\xa0','')

            title    =      soup.select('.a10a3f92e9--container--u51hg')[0].get_text().replace('\xa0','')
            
            try:
            
            
                status   =      soup.select(".a10a3f92e9--container--RXoIe")[0].get_text()
                content  =      (status,price,info,title)
                print(content, url)
            
            
            except Exception as e:
                status   = 'Активно'
                content  =      (status,price,info,title) 
                print(content, url)
            
            logging.info(f'Объявление Циан {url}, Данные получены')


class AvitoParser:
     

    def html_avito_content(url):
            sleep_time = random.uniform(10, 100)
            options.add_argument("--enable-javascript")
            options.add_argument("--headless=new")
            browser  =   webdriver.Chrome(options=options)
            

            browser.get(url)
            browser.add_cookie({"name": "foo", "value": "bar"})
            try:
                status   =  browser.find_element(By.CSS_SELECTOR,'.closed-warning-block-_5cSD').text
                price = browser.find_element(By.CSS_SELECTOR, '.style-item-price-main-jpt3x > span:nth-child(1) > span:nth-child(3) > span:nth-child(1)' ).text

                print(status,price, url)
            except Exception as e:    
                try:
                    status = 'Активно'
                    price = browser.find_element(By.CSS_SELECTOR, '.style-item-price-main-jpt3x > span:nth-child(1) > span:nth-child(3) > span:nth-child(1)' ).text
                    adress = browser.find_element(By.CSS_SELECTOR, '.style-item-address__string-wt61A').text
                    print (price, status, adress, url)
                except Exception as e:
                        print("Объяление было удалено ", url)

            logging.info(f'Объявление Авито {url}, Данные получены')
            browser.quit()

class YandexParser:
     
     def html_yandex_content(url):
        sleep_time = random.uniform(10, 100)
        options.add_argument("--enable-javascript")
        options.add_argument("--headless=new")
        browser  =   webdriver.Chrome(options=options)
        browser.get(url=url)
        browser.add_cookie({"name": "foo", "value": "bar"})
        try:
            price       =   browser.find_element(By.CSS_SELECTOR,'.OfferCardSummaryInfo__price--2FD3C').text
            adress      =   browser.find_element(By.CSS_SELECTOR,'.OfferCardCommercialInfo__title--1QsZP > a:nth-child(1)').text                           
            content     =   (price +' Объявление активно '+ adress)
            print(content, url)
        except Exception as e:
            content = 'Объяление в архиве'
            print(content, url)
        logging.info(f'Объявление Яндекс {url}, Данные получены')    
        browser.close()


