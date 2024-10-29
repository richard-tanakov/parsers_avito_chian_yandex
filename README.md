Python3.12
## Для установки библиотек используйте pipenv 
[pipenv](https://pipenv.pypa.io/en/latest/)



##### Установка пакета pipenv

```sh
sudo apt-get install pipenv 
```

 Установка зависимостей из дериктории parsers_avito_chian_yandex.</p>

`pipenv install --dev`  установка<br>

Выполнить команду 
```sh
cp env.example .env
```


После прописать в .env в переменной db_pass пароль для подключения к базе данных. 


`pipenv graph `  просмотр зависимостей и установленных пакетов <br>
`pipenv shell`    запуск виртуальной среды 


<p>Установленные пакеты</p>



[requests 2.32.3](https://requests.readthedocs.io/en/latest/)<br>
[fastapi 0.115.3](https://fastapi.tiangolo.com/)   <br>
[sqlmodel 0.0.22](https://sqlmodel.tiangolo.com/)<br>
[sqlalchemy 2.0.36](https://www.sqlalchemy.org/)   <br>
[pydantic 2.9.2](https://pypi.org/project/pydantic/)<br>
[sqlalchemy_utils 0.41.2](https://sqlalchemy-utils.readthedocs.io/en/latest/)<br>
[tldextract==5.1.2](https://pypi.org/project/tldextract/)<br>

[bs4==0.0.2](https://pypi.org/project/bs4/)<br>

[webdriver-manager==4.0.2](https://pypi.org/project/webdriver-manager/)<br>
[selenium==4.25.0](https://www.selenium.dev/selenium/docs/api/py/)<br>
[psycopg2==2.9.10](https://pypi.org/project/psycopg2/)<br>



### Запуск FastApi

Из директории parsers_avito_chian_yandex запуск в консоли 

```sh
pipenv shell
```

```sh
fastapi dev fast_api.py 
```
После запуска FastApi доступна  [ссылка на документацию](http://127.0.0.1:8000/docs)

Реализовано, при запросах в FastApi 

1 Добавления объявление в бд 
2 Вывод информации из бд по url и id
3 обновление информации по объявлению 

Осталось реализовать автоматический запуск парсеров. 
и добавление в бд
Отредактировать поиск информации в парсерах. 
Логгирование и ловлю банов. 
