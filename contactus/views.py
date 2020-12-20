from django.shortcuts import render
from .models import Messages
# Create your views here.
def contactus(request):
    if request.method == "POST":
        message = request.POST.get('message')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        print(message,name,email,subject)
        message = Messages(message = message , name = name, email = email, subject = subject)
        message.save()
    return render(request, 'contactus.html', {})