API для социальной сети Yatube
Описание
Проект Yatube API — это интерфейс программирования приложений (API) для социальной сети блогеров Yatube. Он позволяет взаимодействовать с платформой через HTTP-запросы, обеспечивая работу фронтенд-части или мобильного приложения.

Основные возможности:

Публикации: Создание, просмотр, редактирование и удаление постов.

Комментарии: Возможность оставлять отзывы к публикациям и управлять ими.

Сообщества: Просмотр информации о тематических группах.

Подписки: Система подписок на авторов (доступна только аутентифицированным пользователям).

Аутентификация: Работа с пользователями реализована на базе JWT-токенов (библиотека Djoser).

Технологии
Python 3.9

Django 3.2

Django Rest Framework (DRF)

JWT + Djoser

SQLite3

Установка
Клонируйте репозиторий:

Bash
git clone https://github.com/aequu/api-final-yatube-ad.git
cd api-final-yatube-ad
Cоздайте и активируйте виртуальное окружение:

Для Windows:

Bash
python -m venv venv
source venv/Scripts/activate
Для Linux/macOS:

Bash
python3 -m venv venv
source venv/bin/activate
Установите зависимости из файла requirements.txt:

Bash
python -m pip install --upgrade pip
pip install -r requirements.txt
Выполните миграции:

Bash
python manage.py migrate
Запустите проект:

Bash
python manage.py runserver
После запуска проект будет доступен по адресу: http://127.0.0.1:8000/

Примеры запросов
1. Получение JWT-токена
POST /api/v1/jwt/create/

JSON
{
    "username": "ваш_логин",
    "password": "ваш_пароль"
}
В ответ придет access и refresh токены.

2. Получение списка всех публикаций
GET /api/v1/posts/
Запрос может содержать параметры limit и offset для пагинации.

3. Создание новой публикации (только для авторизованных)
POST /api/v1/posts/
Header: Authorization: Bearer <ваш_token>

JSON
{
    "text": "Текст новой публикации",
    "group": 1
}
4. Подписка на автора
POST /api/v1/follow/

JSON
{
    "following": "username_автора"
}
Документация
Полная документация API в формате Redoc будет доступна после запуска сервера по адресу:
http://127.0.0.1:8000/redoc/