from sqlmodel import Field, Session, SQLModel, select
from sqlalchemy import create_engine

from lib import domain_url, normalaze_url, parse_advert
from lib import Advert, CreateUrl
from sqlalchemy.sql.expression import delete

from sqlalchemy_utils import database_exists, create_database
import uuid
import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
load_dotenv()

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time
import random
from typing import Annotated

name_db = os.getenv('name_db')
pass_db = os.getenv('pass_db')
host_db =os.getenv('host_db')
postgr  = os.getenv('postgr')
name_user_db = os.getenv('name_user_db')

db_pass = os.getenv('db_pass')

url_db = f"{postgr}://{name_user_db}:{pass_db}@{host_db}/{name_db}"





def create_engine_advart(url_db):
    """ Создание базы данных при её отсутствии """
    
    if not database_exists(url_db):
        create_database(url_db)
    
    return create_engine(url_db)

 


engine = create_engine_advart(url_db)





x=True


while x == True:
   
   time.sleep(random.randint(1800,3600))
   with Session(engine) as session:
    # получение всех объектов из бд
        adverts = select(Advert)
        adverts = session.exec(adverts)
        for advert in adverts:
            time.sleep(random.randint(15,40))
            updated_advert  =   parse_advert(advert)
            session.add(updated_advert)
            session.commit()
            session.refresh(updated_advert)
            
