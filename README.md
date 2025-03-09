
## Список учасників команди:
- **Годоваий Нікіта(TEAMLEAD)/Hodovanyj Nikita(TEAMLEAD) - https://github.com/Nikita-Hodovanyj**
- **Пілат Віктор /Pilat Viktor - https://github.com/VictorPilat**
- **Гомельская Вікторія/Homelska Viktoria - https://github.com/Viktoria0228**


# Генератор QR-кодів

Наш проект — це веб-сайт, який дозволяє користувачам створювати QR-коди з різними стилями та налаштуваннями. Сайт надає можливість вибору з трьох типів підписок: Free, Standard та Pro, кожна з яких має свої унікальні функції та обмеження. 

## Основні функції:
- **Генерація QR-кодів**: Користувачі можуть створювати QR-коди з різними параметрами, такими як розмір, колір, форма, градієнт, логотип тощо.
- **Три типи підписок**: 
  - **Free**: Базові функції генерації з обмеженням на кількість QR-кодів.
  - **Standard**: Розширені функції, збільшена кількість QR-кодів.
  - **Pro**: Повний доступ до всіх функцій, включаючи преміум-стилі.
- **Історія генерацій**: Користувачі можуть переглядати та керувати своїми раніше згенерованими QR-кодами.
- **Авторизація та реєстрація**: Користувачі можуть зареєструватися та увійти в систему для збереження своїх даних та QR-кодів.

## Використані технології:
- **Django**: Основний фреймворк для розробки веб-додатку.
- **Pillow (PIL)**: Використовується для обробки зображень та створення QR-кодів.
- **SQLite3**: Вбудована база даних для зберігання інформації про користувачів та QR-коди.
- **HTML, CSS, JavaScript**: Використовуються для створення інтерфейсу користувача.
- **GitHub**: Платформа для управління кодом та спільної розробки.

## Як запустити проект локально:
1. Відкрийте проект у вашій IDE.
2. Встановіть всі необхідні модулі, вказані у `requirements.txt`.
3. Запустіть файл `manage.py` за допомогою команди:
   ```bash
   python manage.py runserver
   ```
4. Відкрийте браузер та перейдіть за адресою `http://127.0.0.1:8000/`.

## Як запустити проект на сервері:
Для запуску проекту на сервері рекомендується використовувати хостинг **PythonAnywhere**. Детальні інструкції можна знайти на [офіційному сайті PythonAnywhere](https://www.pythonanywhere.com).

## Структура проекту:
- **base.html**: Головна сторінка сайту.
- **registration.html**: Сторінка для реєстрації нового користувача.
- **authorization.html**: Сторінка для авторизації користувача.
- **free.html, standart.html, pro.html, desktop.html**: Сторінки для генерації QR-кодів з різними параметрами, залежно від обраного плану підписки.

## Приклад функції рендеру сторінок:
```python

def render_contact(request):
    return render(request = request, template_name = "contact/contact.html", context={'footer': True})
```

## Приклад HTML-сторінки (login.html):
```html
{% load static %}

{% block link %}
<link rel="stylesheet" href="{% static 'login/css/login.css' %}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat+Alternates:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">

{% endblock %}


{% block content %}
<header>
    <img src="{% static 'login/img/logo.png' %}" alt="">
    <div class="logo">QREasy</div>
</header>

<body>
    {% if next %}
        <form action="/log/?next={{ next }}" method="post" >
    {% else %}
        <form method="post">
    {% endif %}
       
        {% csrf_token %}
        <h2>Увійти</h2>
        <h3>Ім`я</h3>
        <div class="iconBox">
            <div class="blue"></div>
            <input type="text" name="username" placeholder="name" maxlength="20" required><img src="{% static 'login/img/img4.png' %}" alt="">
        </div>
        <h3>Пароль</h3>
        <div class="iconBox">
            <div class="blue"></div>
            <input class="star" type="password" name="password" placeholder="*******" required><img src="{% static 'login/img/lock.png' %}" alt="">
        </div>
    
        
        {% if user == None %}
            <p style="color: red;">Логін або пароль некоректні</p>  <!-- Invalid email or password -->
        {% endif %}

        <button type="submit">Увійти</button>
        <a href="/reg">Не маєте акаунт?</a>
        </form>
</body>
{% endblock %}

```

## Моделі:
```python

import os
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return os.path.join(instance.user.username, filename)  




class Qrcode(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с аккаунтом
    created_at = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to='img/logos', null=True)
    free = models.BooleanField(default=False)
    standard= models.BooleanField(default=False)
    pro = models.BooleanField(default=False)
    

   


    def __str__(self):
        return f"{self.name} - {self.user.username}"


class QrcodeLimit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Створюємо поля ліміту QR-кодів, які можуть містити лише додатні числа
    limit_standard = models.PositiveBigIntegerField(default=10)
    limit_pro = models.PositiveBigIntegerField(default=20)
```

## URL-адреси:
```python
from django.contrib import admin
from django.urls import path, include
from home import render_home
from home_after import render_home_after
from my_qrcodes import render_my_qrcodes
from contact import render_contact
from login.views import logout_user
from django.conf import settings
from django.conf.urls.static import static
from my_qrcodes import views



from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('', render_home, name = 'home'),
    path('home_after/', render_home_after, name='home_after'),
    path('', include('login.urls'), name="login"),
    path('my_qrcodes/', render_my_qrcodes, name='my_qrcodes'),
    path('contact/', render_contact, name="contact"),
    path('',include("create.urls"), name='create'),
    path('logout/', logout_user, name = "logout"),
    path('delete_qrcode/<int:qrcode_id>/', views.delete_qrcode, name='delete_qrcode'),
    path('',include("home_after.urls"), name='packet_standard'),
    path('',include("home_after.urls"), name='packet_pro'),
    
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

## Приклад сторінки підписки (standard.html):
```html
{% extends 'base.html' %}
{% load static %}

{% block link %}
<link rel="stylesheet" href="{% static 'css/standard.css' %}">
{% endblock %}

{% block title %}
    Створення standard
{% endblock %}


{% block content %}

<body>
    
    <div class="standard">
        <div class="standard2">
            <span class="p1">Standard</span>
            <span class="p2">QR-code</span>
            <span class="p3">12 місяців</span>
        </div>
    </div>

    {% if error %}
        <p class="error-message" style="color: red;">{{ error }}</p>
    {% endif %}

    <div class="main">
        <form method="post">
            {% csrf_token %}
            <h2><img src="{% static 'img/icon_link.png' %}" alt=""> Ваш url-адрес</h2>
            <input class="input-type1" type="text" name="link" placeholder="https://qr-easy-generator.com/" required>
        
            <h2><img src="{% static 'img/icon_name.png' %}" alt=""> Ваша назва</h2>
            <input class="input-type1" type="text" name="name" placeholder="QREasy-код" required>
        
            <h2><img src="{% static 'img/icon_name.png' %}" alt=""> Укажіть розмір QR-коду</h2>
            <input class="input-type4" type="range" name="size" value="150" min = '100' max="300" id="input-range" required>
            <label id= 'range-label' for="input-range">Ширина: 100px</label>

        
            <h2><img src="{% static 'img/icon_name.png' %}" alt=""> Укажіть колір QR-коду</h2>
            <label>Колір шаблону:</label>
            <div class="input-colors">
                <input class="input-type2" type="color" name="color" id= 'color-picker' required>
                <input class="input-type3" type="text" name="color" id= 'color-text' placeholder="#FFFFFF" required>
            </div>

            <label>Колір фону:</label>
            <div class="input-colors">
                <input class="input-type2" type="color" name="back-color" id = 'color-picker1' required>
                <input class="input-type3" type="text" name="back-color" id= 'color-text1' placeholder="#FFFFFF" required>
            </div>
            
            <button class = 'create-st' type="submit">Створити</button>


           

            
        </form>

        
        <div class="qr-code-container">
            <h2>Ваш QR-код:</h2>
            {% if qr_image_url %}
                <img class="QR" src="{{ qr_image_url }}" alt="generated QR-код">
            {% else %}
                <img class="QR" src = "{% static 'img/QR.png' %}" alt="generated QR-код">
            {% endif %}
        </div>

    </div>
    
    <script src="{% static 'js/standart.js'%}"></script>

</body>



{% endblock %}
```

## Чщму саме Django?:
Django — це потужний та універсальний фреймворк для розробки веб-додатків, який став ідеальним вибором для нашого проекту генератора QR-кодів.

## Висновки:
Під час цого проекту мі здобули величезний досвід, вивчили нові технології та покращили навички роботи з Django, Pillow, SQLite3, HTML, CSS та JavaScript. Ми також покращили нашу комунікацію та розуміння коду, що дозволило нам створити функціональний та зручний у використанні веб-додаток для генерації QR-кодів.