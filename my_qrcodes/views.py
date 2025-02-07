from django.shortcuts import render
 
def render_my_qrcodes(request):
  qr_image_url = request.session.get('qr_image_url')
  user_name = request.session.get('user_name')
  return render( request,'my_qrcodes/my_qrcodes.html', context = {'qr_image_url': qr_image_url, 'user_name': user_name, 'footer': True})