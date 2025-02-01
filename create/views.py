import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.shortcuts import render
from .models import Qrcode
from django.contrib.auth.decorators import login_required
import os




@login_required
def render_free(request):
    qr_image_url = None  # Переменная для хранения URL картинки

    if request.method == "POST":
        name = request.POST.get("name")
        link = request.POST.get("link")

        if not name or not link:
            return render(request, "free.html", {"error": "Заполните все поля", "footer": True})

        print(f"Генерация QR-кода для: {link}")

        try:
            qr_code = Qrcode(name=name, link=link, user=request.user)

            # Генерация QR-кода
            qr = qrcode.make(link)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")

            # Проверяем папку перед сохранением
            
            path = os.path.join("media", "qr_codes")
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Создана папка: {path}")

            # Сохранение изображения в модель
            filename = f"{name}.png"
            qr_code.image.save(filename, ContentFile(buffer.getvalue()), save=True)
            qr_code.save()

            # Получаем URL для отображения в шаблоне
            qr_image_url = qr_code.image.url
            print(f"QR-код сохранен и доступен по пути: {qr_image_url}")

        except Exception as e:
            print(f"Ошибка при создании QR-кода: {e}")

    return render(request, "free.html", {"qr_image_url": qr_image_url, "footer": True})




def render_standard(request):
    return render(request, 'standard.html',{'footer': True})

def render_pro(request):
    return render(request, 'pro.html', {'footer': True})