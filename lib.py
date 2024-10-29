
import tldextract
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
import uuid
from pydantic import  BaseModel
from par import ParserCian
import datetime
import ParserYandex
import ParserAvito




class CreateUrl(BaseModel):
     url : str

class Advert(SQLModel, table =True):
    """ Объект модели объявления """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True, description = 'Сгенерированый уникальный uuid ')
    url :str = Field(nullable=False, index=True, description    = 'Url ссылка на объявление')
    source_type : str = Field(nullable=False, index= True, description  = 'Наименование сайта, где опублековано объявление')
    last_check_ts : str | None = None
    is_publicated : bool| None = None
    price : str | None = None

def date_time():
        """ Получение текущего времени и даты """


        now_date_time = datetime.datetime.now()
        return now_date_time.strftime("%H:%M:%S %d-%m-%Y")
       


def domain_url(url:str):
    """ Получение домена """


    url_componens = tldextract.extract(url)

    if url_componens.domain == 'ya' or url_componens.domain == 'yandex':
            return 'Yandex'    
    if url_componens.domain == 'avito':
        return "Avito"
    if url_componens.domain == 'cian':
            return "Cian"
    else:
            return None
    

def normalaze_url(url:str):
        """Приводит url к каноническому виду """      
        
        if url[-1] =='/':
                norm_url = url[0:-1] 
                return norm_url
        else:
               norm_url = url
               return norm_url

def parse_advert(advert: Advert)->Advert:
    
    """ Определение с какого сайта объявление,
        И обновление его данных
    """ 
    
    site = advert.source_type
    

    match site:
            case 'Yandex':

                price, is_published = ParserYandex.yandex_parser(url=advert.url)
                
                
                advert.last_check_ts = date_time()
                advert.price = price
                advert.is_publicated = is_published
                return advert

    
            case "Avito":
                price, is_published = ParserAvito.parse_avito(url=advert.url)
                
                
                advert.last_check_ts = date_time()
                advert.price = price
                advert.is_publicated = is_published
                return advert

            
            
            
            case "Cian":
                
                parser = ParserCian(url=advert.url)
                price, is_published = parser.parse()
                advert.last_check_ts = date_time()
                advert.price = price
                advert.is_publicated = is_published
                return advert

def start_parsers():
    """ Достает все url из базы данных  """   
          

