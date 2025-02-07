import os
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings  # Импортируем settings для MEDIA_ROOT
from .models import Qrcode

@login_required
def render_free(request):
    if request.method == "POST":
        name = request.POST.get("name")
        link = request.POST.get("link")

        if not name or not link:
            return render(request, "free.html", {"error": "Заполните все поля", "footer": True})

        try:
            username = request.user.username
            user_qr_folder = os.path.join(settings.MEDIA_ROOT, username)

            if not os.path.exists(user_qr_folder):
                os.makedirs(user_qr_folder)

            qr = qrcode.make(link)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")

            filename = f"{name}.png"
            file_path = os.path.join(user_qr_folder, filename)

            with open(file_path, "wb") as f:
                f.write(buffer.getvalue())

            
            qr_code = Qrcode(name=name, link=link, user=request.user)
            qr_code.image.save(f"{username}/{filename}", ContentFile(buffer.getvalue()), save=True)

            request.session["qr_image_url"] = f"/media/{username}/{filename}"

            

        except Exception as e:
            return render(request, "free.html", {"error": f"Ошибка: {e}", "footer": True})

    return render(request, "free.html", {"footer": True})

@login_required
def render_standard(request):
    if request.method == "POST":
        name = request.POST.get("name")
        link = request.POST.get("link")
        color = request.POST.get("color", "black")

        if not name or not link:
            return render(request, "standard.html", {"error": "Заполните все поля", "footer": True})

        try:
            username = request.user.username
            user_qr_folder = os.path.join(settings.MEDIA_ROOT,  username)

            if not os.path.exists(user_qr_folder):
                os.makedirs(user_qr_folder)

            qr = qrcode.QRCode()
            qr.add_data(link)
            qr.make(fit=True)

            img = qr.make_image(fill_color=color, back_color="white")

            buffer = BytesIO()
            img.save(buffer, format="PNG")

            filename = f"{name}.png"
            file_path = os.path.join(user_qr_folder, filename)

            with open(file_path, "wb") as f:
                f.write(buffer.getvalue())

            
            qr_code = Qrcode(name=name, link=link, user=request.user)
            qr_code.image.save(f"{username}/{filename}", ContentFile(buffer.getvalue()), save=True)

            request.session["qr_image_url"] = f"/media/{username}/{filename}"

           

        except Exception as e:
            return render(request, "standard.html", {"error": f"Ошибка: {e}", "footer": True})

    return render(request, "standard.html", {"footer": True})


def render_pro(request):
    return render(request, 'pro.html', {'footer': True})