from django.shortcuts import render

def render_home_after(request):
  return render(request = request, template_name = "home_after/home_after.html", context={'footer': True} )