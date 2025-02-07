import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.shortcuts import render
from .models import Qrcode
from django.contrib.auth.decorators import login_required
import os
from PIL import Image
from datetime import datetime



@login_required
def render_free(request):
    qr_image_url = None  

    if request.method == "POST":
        name = request.POST.get("name")
        link = request.POST.get("link")

        if not name or not link:
            return render(request, "free.html", {"error": "Заполните все поля", "footer": True})

        print(f"Генерация QR-кода для: {link}")
        try:
            username = request.user.username
            user_qr_folder = os.path.join("media", username)

            if not os.path.exists(user_qr_folder):
                os.makedirs(user_qr_folder)
                print(f"Создана папка: {user_qr_folder}")

            qr_code = Qrcode(name=name, link=link, user=request.user)
            qr = qrcode.make(link)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")

            filename = f"{name}.png"
            file_path = os.path.join(user_qr_folder, filename)

            with open(file_path, "wb") as f:
                f.write(buffer.getvalue())

        
            qr_code.image.name = f"{username}/{filename}"
            qr_code.save()

            qr_image_url = f"/media/{username}/{filename}"
            print(f"QR-код сохранен и доступен по пути: {qr_image_url}")

        except Exception as e:
            print(f"Ошибка при создании QR-кода: {e}")

    return render(request, "free.html", {"qr_image_url": qr_image_url, "footer": True})

    





@login_required
def render_standard(request):
    qr_image_url = None  

    if request.method == "POST":
        name = request.POST.get("name")
        link = request.POST.get("link")
        size = request.POST.get("size")
        color = request.POST.get("color")

        if not name or not link or not size or not color:
            return render(request, "standard.html", {"error": "Заполните все поля", "footer": True})

        try:
        
            size = int(size)  

            username = request.user.username
            user_qr_folder = os.path.join("media", username)

            if not os.path.exists(user_qr_folder):
                os.makedirs(user_qr_folder)

            qr_code = Qrcode(name=name, link=link, user=request.user)

            
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,  
                border=2,
            )
            qr.add_data(link)
            qr.make(fit=True)

            
            img = qr.make_image(fill_color=color, back_color="white").convert("RGB")

            
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
            return render(request, "standard.html", {"error": f"Ошибка: {e}", "footer": True})

    return render(request, "standard.html", {
        "qr_image_url": qr_image_url,
        "footer": True
    })





def render_pro(request):
    return render(request, 'pro.html', {'footer': True})