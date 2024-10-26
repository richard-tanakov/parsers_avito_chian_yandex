
import tldextract
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
import uuid
from datetime import datetime, timezone
from pydantic import  BaseModel
from parsers import ParserCian


class CreateUrl(BaseModel):
     url : str

class Advert(SQLModel, table =True):
    """ Объект модели объявления """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True, description = 'Сгенерированый уникальный uuid ')
    url :str = Field(nullable=False, index=True)
    source_type : str = Field(nullable=False, index= True)
    last_check_ts : datetime = Field(nullable = True, index=True)
    is_publicated : bool| None = None
    price : float| None = None




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
                norm_url = url
                return norm_url
        else:
               norm_url = url+'/'
               return norm_url

def parse_advert(advert: Advert)->Advert:
    """ Определение с какого сайта объявление,
        И обновление его данных
    """
    site = advert.source_type
    match site:
            case 'Yandex':
                return 'ya'
            
            case "Avito":
                return 'Avito'
            case "Cian":
                parser = ParserCian(url=advert.url)
                price, is_published = parser.parse()
                advert.price = price
                advert.is_publicated = is_published
                return advert

                

