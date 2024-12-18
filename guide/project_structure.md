# Структура проекта

Проект состоит из главной директории и второстепенных.

Основная директория проекта - `client_app`. Django работает с нашим кодом через неё.

В ней находятся:

`manage.py`: основной файл для управления проектом через командную строку. Используется для запуска сервера, миграций базы данных, создания приложений и т.д.

`~/src/client_app/` (папка с именем проекта):

`settings.py`: главный файл настроек вашего проекта. Здесь вы указываете базы данных, приложения, настройки безопасности и прочее. <br>
`urls.py`: файл для маршрутизации (роутинг) запросов. Содержит информацию о том, какой URL должен быть связан с каким представлением (view).

Во второстепенных директориях у нас находится логика, относящаяся к сущностям проекта:
- `cars` - все что связано с самим автомобилем;
- `comments` - все что относится к комментариям;
- `orders` - все что относится к заказам;
- `options` - все что относится к дополнительным услугам;
- `prices` - все что относится к тарифам и цене;

Все они будут иметь одинаковую структуру:
```
├── cars/
│   ├── migrations/     # Миграции - логи о том, что делали с базой данных
│   ├── enums/          # Папка с информацией о постоянных значениях, как константы - только по группам
│   ├── __init__.py     # Дает Python понять, что папка - модуль (на данном этапе это не важно)
│   ├── admin.py        # Файл для настройки интерфейса Django admin. Здесь вы регистрируете модели для управления через административную панель.
│   ├── apps.py         # Файл конфигурации модуля (на данном этапе это не важно))
│   ├── models.py       # Здесь определяются модели данных, которые будут отражать структуру базы данных (таблицы).
│   ├── tests.py        # Файл для написания тестов модуля (на данном этапе это не важно)
│   ├── views.py        # Файл, в котором находятся логика обработки запросов
│   ├── urls.py         # Содержит информацию об эндпоинтах, за которые этот модуль отвечает
│   ├── serializers.py  # Преобразует данные в JSON и обратно
```