from django.shortcuts import render
from .models import Qrcode


def render_free(request):
    
    return render(request, 'free.html',{'footer': True})
# Create your views here.
def render_standard(request):
    return render(request, 'standard.html',{'footer': True})

def render_pro(request):
    return render(request, 'pro.html', {'footer': True})