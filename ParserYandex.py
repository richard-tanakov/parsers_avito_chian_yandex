from time import sleep
import random
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re


import json



     
def yandex_parser(url):
        

        #sleep(random.randint(30,60))
            headers = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
        
            options = Options()
            options.add_argument('--no-sandbox')
           
            options.add_argument('--headless')
            options.add_argument('--enable-javascript')
            
            #options.page_load_strategy = 'normal' 
        
            driver = webdriver.Chrome(options=options)  
              
            
            try:
                   

                    

                    driver.get(url)
                    
                    
                    pr =driver.find_element(By.PARTIAL_LINK_TEXT,"₽").text
                    price = (pr[:pr.find('₽')])                    
                    is_publicated = True
                    status = 'successful request'
                    price = price
                    

                    return price,is_publicated

            except Exception as e:
                    status = 'unavailable' 
                    price = 0
                    is_publicated = False


                    return price,is_publicated 
            
        
     
   

