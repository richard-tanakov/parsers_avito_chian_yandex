Ссылки на документации в конце файла. 



Для парсинга авито используется selenium так как там возникает переодически капча, также он отлично эмитирует поведение пользователя в браузере. 
Обход капчи пока вопрос открытый -- Добавил включение Javascript. Нужен тест запросов. 



Для установки всех использоваемых библиотек 


Используйте команду--  pipenv install  --из дериктории  real_estate_transaction

Чтобы установить pipenv -- sudo apt-get install pipenv



Библиотеки установятся из файла Pipfile


Для парсера циан используется requests и bs4.




База данных можно использовать sqlite3, если будут несколько человек пользоваться можно использовать Turso удалённая база. 


selenium -- https://selenium-python-api-docs.readthedocs.io/en/latest/api.html
rich -- https://rich.readthedocs.io/en/stable/introduction.html
requests -- https://requests.readthedocs.io/en/latest/index.html
bs4 -- https://beautiful-soup-4.readthedocs.io/en/latest/


Пометка на будующие при включение исполнения JavaScript options.add_argument("--enable-javascript")

в селениум капча вылазиет намного реже


Реализумые задачи. 
1. Рефакторин, перенос по классам парсеры в файл Options.py 
2.  привести все получаемые данные к единому формату для записи. Создание базы 
3. добавить пловерки на капчу.
4. Решить долбанные блокировки ( поставил рандомное прерывание возможно авито перестанет блочить ip)