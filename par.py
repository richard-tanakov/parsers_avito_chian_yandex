
from requests import Response, get 
from bs4 import BeautifulSoup 
from time import sleep
import random
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from typing import Dict
import re







options = ChromeOptions()




class ParserCian:
    url : str
    response : Response
    headers : Dict[str,str]

    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
        self.response = self.get_url()
        

    def get_url(self) ->Response:   
        sleep_time = random.uniform(10, 100)
        sleep(sleep_time)
        response    =   get(url= self.url, headers=self.headers)
        
        
        if response.status_code == 404:
        
                print("Объявление удалено", self.url)
        
        
        
        return response 
        



    def html_chian_content(self):
            """ Получение контента """            
            soup     =      BeautifulSoup(self.response.content, 'html.parser')

            price    =      soup.select('.a10a3f92e9--amount--ON6i1 > span:nth-child(1)')[0].get_text().replace('\xa0','')

            #info  =      soup.select('.a10a3f92e9--address-line--GRDTb > div:nth-child(1)')[0].get_text().replace('\xa0','')

            #title    =      soup.select('.a10a3f92e9--container--u51hg')[0].get_text().replace('\xa0','')
            
            price = float(re.search(r'\d+', price).group())
            try:
            
            
                status    =      soup.select(".a10a3f92e9--container--RXoIe")[0].get_text()
                content  =      (status ,price)
                return content
            
            
            except Exception as e:
                status   = 'Активно'
                content  =     (status,price) 
                return content
            
           

    def parse(self):
         
        status, price = self.html_chian_content()
        if (status == 'Активно'):
             is_published = True
        else:
             is_published = False    
        return (price, is_published)             






