from django.shortcuts import render, redirect


def render_home_after(request):



  return render(request = request, template_name = "home_after/home_after.html", context={'footer': True} )

def render_packet_pro(request):
  from create.models import Qrcode, QrcodeLimit

  packet_pro = True    

  qrcode_limit, created = QrcodeLimit.objects.get_or_create(user=request.user)
  
  if request.method == "POST" and 'quantity_button' in request.POST:
      if request.user.is_authenticated:
          quantity = request.POST.get('quantity')
          # Перетворюємо значення quantity на число, адже воно отримується як рядок з POST
          quantity = int(quantity)  
          if quantity > 0:
              # Оновлюємо ліміт та зберігаємо в базі даних
              qrcode_limit.limit_pro += quantity 
              qrcode_limit.save()
              success_message = f"Ваш ліміт збільшено на {quantity}. Новий ліміт: {qrcode_limit.limit_pro}"
              print(success_message)


 
  return render(request = request, template_name = "home_after/packet_pro.html", context={'footer': True, 'packet_pro': packet_pro} )

def render_packet_standard(request):
  from create.models import Qrcode, QrcodeLimit
  packet_standart = True

  qrcode_limit, created = QrcodeLimit.objects.get_or_create(user=request.user)
  # Початковий ліміт
  # user_qr_limit = qrcode_limit.limit_standart
  
  if request.method == "POST" and 'quantity_button' in request.POST:
      if request.user.is_authenticated:
          quantity = request.POST.get('quantity')
          # Перетворюємо значення quantity на число, адже воно отримується як рядок з POST
          quantity = int(quantity)  
          if quantity > 0:
              # Оновлюємо ліміт та зберігаємо в базі даних
              qrcode_limit.limit_standard += quantity 
              qrcode_limit.save()
              success_message = f"Ваш ліміт збільшено на {quantity}. Новий ліміт: {qrcode_limit.limit_standard}"
              print(success_message)


 
  return render(request = request, template_name = "home_after/packet_standard.html", context={'footer': True, 'packet_standart': packet_standart} )