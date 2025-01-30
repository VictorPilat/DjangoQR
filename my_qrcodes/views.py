from django.shortcuts import render

def render_my_qrcodes(request):
  return render(request = request, template_name = 'my_qrcodes/my_qrcodes.html')