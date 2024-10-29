from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options






     
def yandex_parser(url):
        
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
            
        
     
   

