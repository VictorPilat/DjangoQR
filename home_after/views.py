from django.shortcuts import render, redirect


def render_home_after(request):
  from create.models import Qrcode
  # if 'pro-modal' in request.POST:
  #   # pro = Qrcode.objects.create()
    
  # elif 'standart-modal' in request.POST:
  #   pass
    
  return render(request = request, template_name = "home_after/home_after.html", context={'footer': True} )

def render_packet_pro(request):
  # if request.method == 'POST':
    

 
  return render(request = request, template_name = "home_after/packet_pro.html", context={'footer': True} )

def render_packet_standard(request):
  # if request.method == 'POST':
    

 
  return render(request = request, template_name = "home_after/packet_standard.html", context={'footer': True} )