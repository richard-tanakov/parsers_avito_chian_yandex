from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
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
from fastapi.responses import JSONResponse

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
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)



def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()    


     

@app.post("/urls/")
def create_url(create_url:CreateUrl, session:SessionDep) -> Advert:

    domain =  domain_url(create_url.url)
    norm_url = normalaze_url(create_url.url)
    advert = session.exec(select(Advert).where(Advert.url == norm_url)).first()
    if (domain is None):
        raise HTTPException (status_code = 422, detail = 'неккоректный url')
    if  not advert:
    
    
    

        advert   = Advert(
            source_type =   domain, 
            url         =   norm_url
        ) 
        session.add(advert)
        session.commit()
        session.refresh(advert)
        return advert 
    return JSONResponse (status_code = 404, content ={'messange':'Повторное добавление url'})



@app.get('/urls/{id}')
def read_url_by_uuid(id : str, session : SessionDep) -> Advert:
    #обращение к бд и возвращение объекта. 
    advert = session.get(Advert, id)
    if not advert:
        raise HTTPException(status_code=404, detail="Запись не найдена")
    return advert 

@app.get('/urls/')
def read_url_by_url(url:str, session:SessionDep) -> Advert:
    #обращение к бд и возвращение объекта. 
    urls = normalaze_url(url)
    advert = session.exec(select(Advert).where(Advert.url== urls)).first()
    if not advert:
        raise HTTPException(status_code=404, detail="Запись не найдена")
    return advert 


@app.patch('/urls/{id}')
def update_url_by_uuid(id:str, session: SessionDep) ->Advert:
    """ Получение данных по id """
    advert = session.get(Advert, id)
    if not advert:
        raise HTTPException(status_code=404, detail="Запись не найдена")
     
    #получение  данных перезапись в бд вывод из неё данных

    updated_advert  =    parse_advert(advert)
    
    session.commit()
    session.refresh(updated_advert)
        
     
    return updated_advert 


@app.patch('/urls/')
def update_url_by_url(url:str, session : SessionDep) ->Advert :
    
      
    #""" Получение данных по url """
    advert = session.exec(select(Advert).where(Advert.url == url)).first()
    
    
    if not advert: 
        raise HTTPException(status_code=404, detail="Запись не найдена")
        #получение  данных, перезапись в бд вывод из неё данных
    
    updated_advert  =   parse_advert(advert)
    session.add(updated_advert)
    session.commit()
    session.refresh(updated_advert)
    
    return updated_advert




@app.delete('/urls/{id}')
def delete_url(id : str,  session : SessionDep):
    """ Удаление записи из базы данных """
    advert_delete =session.get(Advert, id)

    session.delete(advert_delete)   
    session.commit() 

    return "Объявление удалено"

