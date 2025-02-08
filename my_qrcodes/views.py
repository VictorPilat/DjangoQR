
from django.shortcuts import render


def render_my_qrcodes(request):
    from create.models import Qrcode 
    user_qrcodes = Qrcode.objects.filter(user=request.user)  
    return render(request, 'my_qrcodes/my_qrcodes.html', {
        'user_qrcodes': user_qrcodes,  
        'footer': True
    })

