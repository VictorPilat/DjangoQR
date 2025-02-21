from django.shortcuts import render

def render_home(request):
  return render(request = request, template_name = "home/home.html")
