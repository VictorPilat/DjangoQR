import qrcode, pyqrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask

from qrcode.image.styles.moduledrawers import *
from io import BytesIO
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .models import Qrcode
from django.contrib.auth.decorators import login_required
import os
from PIL import Image
from datetime import datetime




def render_free(request):
    qr_image_url = None  

    if request.method == "POST":
        name = request.POST.get("name")
        link = request.POST.get("link")

        if not name or not link:
            return render(request, "free.html", {"error": "Заповніть усі поля", "footer": True})

        print(f"Генерация QR-кода для: {link}")
        file_path = None
        try:

            if request.user.is_authenticated:
                username = request.user.username
            else:
                username = 'anonymous'

            user_qr_folder = os.path.join("media", username)

            if not os.path.exists(user_qr_folder):
                os.makedirs(user_qr_folder)
                print(f"Создана папка: {user_qr_folder}")

                 
            qr = qrcode.make(link)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")

            filename = f"{name}.png"
            file_path = os.path.join(user_qr_folder, filename)

            with open(file_path, "wb") as f:
                f.write(buffer.getvalue())
         # Якщо користувач не залогінений, то request.user буде AnonymousUser, 
            # який не має атрибута username
            if request.user.is_authenticated:
                qr_code = Qrcode(name=name, link=link, user=request.user)
                qr_code.image.name = f"{username}/{filename}"
                qr_code.save()
           


            qr_image_url = f"/media/{username}/{filename}"
            print(f"QR-код сохранен и доступен по пути: {qr_image_url}")



        except Exception as e:
            print(f"Ошибка при создании QR-кода: {e}")

    return render(request, "free.html", {"qr_image_url": qr_image_url, "footer": True})

    




# @login_required - Показує цю сторінку лише при тому, що користувач залогінений
# В іншому випадку login_url перенаправляє на сторінку login.
# А після успішної реєстрації перенаправляє на сторінку нашого пакету
# Тобто на сторінку, яку користувач хотів відвідати перед login
@login_required(login_url='login')
def render_standard(request):
    qr_image_url = None  

    if request.method == "POST":
        name = request.POST.get("name")
        link = request.POST.get("link")
        size = request.POST.get("size")
        color = request.POST.get("color")
        back_color = request.POST.get("back-color")

        if not name or not link or not size or not color:
            return render(request, "standard.html", {"error": "Заповніть усі поля"})

        try:
        
            size = int(size)  

            username = request.user.username
            user_qr_folder = os.path.join("media", username)

            if not os.path.exists(user_qr_folder):
                os.makedirs(user_qr_folder)

            qr_code = Qrcode(name=name, link=link, user=request.user)

            
            qr = qrcode.QRCode(
                version=2,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,  
                border=2,
            )
            qr.add_data(link)
            qr.make(fit=True)

            
            img = qr.make_image(fill_color=color, back_color= back_color)

            
            img = img.resize((size, size), Image.NEAREST)

            
            buffer = BytesIO()
            img.save(buffer, format="PNG")

            filename = f"{name}_{datetime.now().timestamp()}.png"  
            file_path = os.path.join(user_qr_folder, filename)

            with open(file_path, "wb") as f:
                f.write(buffer.getvalue())

            qr_code.image.name = f"{username}/{filename}"
            qr_code.save()

            qr_image_url = f"/media/{username}/{filename}"

        except Exception as e:
            print(e)
        return redirect('my_qrcodes')

    return render(request, "standard.html", {
        "qr_image_url": qr_image_url,
        "footer": True
    })


# Функція перетворення hex формат на rgb. 
# Потрібна для того, щоб користувач міг ввести значення hex
def hex_to_rgb(hex_format):
    # Прибираємо "#", щоб уникнути помилки 'invalid literal for int() with base 16: '#f''
    hex_format = hex_format.lstrip('#') 
    return tuple(int(hex_format[i:i+2], 16) for i in (0, 2, 4))


@login_required(login_url='login')
def render_pro(request):
    qr_image_url = None  

    if request.method == "POST":
        name = request.POST.get("name")
        link = request.POST.get("link")
        size = request.POST.get("size")
        color = hex_to_rgb(request.POST.get("color"))
        back_color = hex_to_rgb(request.POST.get("back_color"))
        pattern = request.POST.get("pattern")
        logo = request.FILES.get("logo")
        # eye_frame = request.POST.get("eye-frame")

        if not name or not link or not size or not color:
            return render(request, "standard.html", {"error": "Заповніть усі поля"})

        try:
        
            size = int(size)  

            username = request.user.username
            user_qr_folder = os.path.join("media", username)


            if not os.path.exists(user_qr_folder):
                os.makedirs(user_qr_folder)

            qr_code = Qrcode(name=name, link=link, user=request.user)


        
           
            pattern_modules = {
                "default": SquareModuleDrawer(),
                "squares": GappedSquareModuleDrawer(),
                "dots": CircleModuleDrawer(),
                "rounded": RoundedModuleDrawer(),
                "vertical_lines": VerticalBarsDrawer(),
                "horizontal_lines": HorizontalBarsDrawer(),
            }

            #  Задаємо стандартний шаблон
            module_drawer = pattern_modules.get(pattern, SquareModuleDrawer())

            # eye_modules = {
            #     "default": SquareModuleDrawer(),
            #     "dot": CircleModuleDrawer(),
            #     "rounded": RoundedModuleDrawer(),
            #     "gapped": GappedSquareModuleDrawer(),
            # }

            # eye_drawer = eye_modules.get(eye_frame, SquareModuleDrawer())

            
            qr = qrcode.QRCode(
                version=5,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,  
                border=4,
            )


            qr.add_data(link)
            qr.make(fit=True)

       

            
            img = qr.make_image(
                image_factory= StyledPilImage, 
                color_mask = SolidFillColorMask(back_color=back_color, front_color=color),
                module_drawer = module_drawer, 
            )


            img = img.resize((size, size), Image.NEAREST)

            
            buffer = BytesIO()
            img.save(buffer, format="PNG")

            filename = f"{name}_{datetime.now().timestamp()}.png"  
            file_path = os.path.join(user_qr_folder, filename)

            with open(file_path, "wb") as f:
                f.write(buffer.getvalue())

            qr_code.image.name = f"{username}/{filename}"
            qr_code.save()

            qr_image_url = f"/media/{username}/{filename}"


             # Додаємо логотип, якщо додає користувач
            if logo:
                #
                width, height = img.size
                # Відкриваємо картинку логотипу 
                logo_img = Image.open(logo)
                # Конвертуємо в формат RGBA, щоб за наявністю фону в картинці логотипу,
                # зробити його прозорим
                logo_img = logo_img.convert("RGBA")
                # Задаємо розмір логотипу в qr-коді
                logo_size = 40
                # Обчислюємо центр Qr-коду та логотипу по горизонталі вертикалі
                xmin = ymin = int((width / 2) - (logo_size / 2))
                xmax = ymax = int((height / 2) + (logo_size / 2))
                # Масштабуємо логотип 
                logo_img = logo_img.resize((xmax - xmin, ymax - ymin))
                # Вставляємо логотип у qr-код
                img.paste(logo_img, (xmin, ymin, xmax, ymax), mask = logo_img)
                img.save(file_path, format="PNG")

            
            


        except Exception as e:
            print(e)
        return redirect('my_qrcodes')


    return render(request, 'pro.html', {"qr_image_url": qr_image_url, 'footer': True})