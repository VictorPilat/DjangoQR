
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required



# @login_required
def render_my_qrcodes(request):
    from create.models import Qrcode 
    
    user_qrcodes = Qrcode.objects.filter(user=request.user)
   
    return render(request, 'my_qrcodes/my_qrcodes.html', {
        'user_qrcodes': user_qrcodes,  
        'footer': True
    })


@login_required
def delete_qrcode(request, qrcode_id):
    from create.models import Qrcode 
    qrcode = get_object_or_404(Qrcode, id=qrcode_id, user=request.user)
    
    
    if qrcode.image:
        if default_storage.exists(qrcode.image.name):
            default_storage.delete(qrcode.image.name)
    

    qrcode.delete()
    
    return redirect('my_qrcodes') 