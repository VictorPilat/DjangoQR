
from django.shortcuts import render
# from create.models import Qrcode
from django.contrib.auth.decorators import login_required







def render_my_qrcodes(request):
    # Получаем только QR-коды текущего пользователя
    print(request.user)  # Проверим, кто текущий пользователь

    from create.models import Qrcode  # Импорт модел
    user_qrcodes = Qrcode.objects.filter(user=request.user)  
    return render(request, 'my_qrcodes/my_qrcodes.html', {
        'user_qrcodes': user_qrcodes,  # Передаем в шаблон только свои QR-коды
        'footer': True
    })

