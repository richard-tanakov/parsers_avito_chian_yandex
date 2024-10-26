from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
import uuid
from datetime import datetime, timezone
from pydantic import  BaseModel
from lib import domain_url, normalaze_url, parse_advert
from lib import Advert, CreateUrl





sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

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
    
    if (domain is None):
        raise HTTPException (status_code = 422, detail = 'неккоректный url')
    norm_url = normalaze_url(create_url.url) 
    advert   = Advert(
        source_type =   domain, 
        url         =   norm_url
    ) 
    session.add(advert)
    session.commit()
    session.refresh(advert)
    return advert 



@app.get('/urls/{id}')
def read_url_by_uuid(id : str, session : SessionDep) -> Advert:
    #обращение к бд и возвращение объекта из бд. 
    advert = session.get(Advert, id)
    if not advert:
        raise HTTPException(status_code=404, detail="Запись не найдена")
    return advert 


@app.get('/urls/')
def read_url_by_url(url:str, session:SessionDep) -> Advert:
    #обращение к бд и возвращение объекта из бд. 

    advert = session.exec(select(Advert).where(Advert.url== url)).first()
    if not advert:
        raise HTTPException(status_code=404, detail="Запись не найдена")
    return advert 


@app.patch('/urls/{id}')
def update_url_by_uuid(id:str, session: SessionDep):
    advert = session.get(Advert, id)
    if not advert:
        raise HTTPException(status_code=404, detail="Запись не найдена")
     
    #получение  данных перезапись в бд вывод из неё данных

    updated_advert  =    parse_advert(advert)
    session.add(updated_advert)
    session.commit()
    session.refresh(updated_advert)
        
     
    return updated_advert 

@app.patch('/urls/')
def update_url_by_url(url:str) ->Advert:
    #1 нахождение в бд проверка сосуществования. 
    # Yes получения домена по url
    # определние пути парсера. 
    #получение  данных перезапись в бд вывод из неё данных
    return Advert(url=url)

@app.delete('/urls/')
def delete_url(uuid : str) -> None:
    #Поиск записи по id далее её удаление
    return None

