# HammerTest
# API
url | метод запроса | описание | входные данные | выходные данные
--- | --- | --- | --- | --- |
http://127.0.0.1:8000/api/docs/#/|get|тут находится swagger для тестирования api|-|-
http://127.0.0.1:8000/api/invite|put|Эндпоинт для использования инвайт-кода|{"invite_code": "string","phone_number": "string"}|-|
http://127.0.0.1:8000/api/user/{id}|get|Возвращает данные о пользователе id  которого ввели| - | {"id": 1,"phone_number": "9961350426","invite_code": "3cmZXE","used_invite_code": null,"users": [{"id": 2,"phone_number": "77777777777","invite_code": "RKahst","used_invite_code": "3cmZXE"}]}
http://127.0.0.1:8000/api/users|post|Создает пользователя возвращая jwt  токен|{"phone_number": "string","password": "string"}|
http://127.0.0.1:8000/api/token|post|получение  jwt  токена по паролю и номеру телефона|{"username": "string","password": "string"}|{"access": "string","refresh":"string"}
http://127.0.0.1:8000/api/refresh|post|обновление токена по  refresh  токену|{"refresh": "string"}|{"access": "string"}
http://127.0.0.1:8000/api/refresh|post|проверка токена на валидность|{"token": "string"}|-


## Как запустить 
1. ## Скачать репозиторий
    
    ```bash
    git clone https://github.com/S1stemus/HammerTest
    ```
2. ## Перейти в папку репозитория cd 
    ```bash
    cd HammerTest
    ```    
3. ## Выполнить команду
    ```bash
     sudo docker compose up
    ``` 



