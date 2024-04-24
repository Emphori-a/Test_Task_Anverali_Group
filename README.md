## Биржа заказов

### Описание:
Сайт биржа заказов в рамках выполнения тестового задания для компании Anverali Group. Реализованы CRUD операции для заказов, а также логика для двух ролей пользователей: Заказчика и Исполнителя.

### Использованные технологии:

Python 3.9
Django 4
PostgreSQL 13

### Запуск проекта

1) Создать БД Postgre для использования в приложении.
2) В корне проекта создать файл .env и указать в нем следующие настройки:
    - SECRET_KEY=django-insecure-)4cgqjgc@3-9xt2p+q26%ps%#&k!t03^)fu99f0j!8$1!8l1hw
    - NAME - имя созданной БД
    - USER - имя пользователя БД
    - PASSWORD - пароль пользователя БД
    - HOST - хост для подключения к БД
    - PORT - порт для подключения к БД
3) Создать и активировать виртуальное окружение.

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```
4) Установить зависимости из файла requirements.txt

```
pip install -r requirements.txt
```

5) Выполнить миграции

```
python3 manage.py migrate
```

6) Запустить проект

```
python3 manage.py runserver
```

7) Опционально: загрузить фикстуры тестовыми данными для БД:

```
python manage.py loaddata db.json 
```

### Автор, контактная информация:

Мартынова Валерия
* e-mail: emphoria@yandex.ru
* @Emphori