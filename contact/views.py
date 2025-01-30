from django.shortcuts import render

# Create your views here.
def render_contact(request):
    return render(request = request, template_name = "contact/contact.html")