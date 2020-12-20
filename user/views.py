from django.shortcuts import render, redirect
from .models import Users
# Create your views here.
def login(request):
    if 'username' in request.session:
        return redirect('cart')
    if request.method == "POST":
        user = Users
        email = request.POST.get('email')
        password = request.POST.get('password')
        queryset = user.objects.get(email = email)
        if(queryset.password == password):
            print("login successful")
            request.session['username'] = queryset.name
            request.session['email'] = email
            return redirect('index')

        else:
            print("login unsuccessful")

    return render(request, 'login.html',{})

def logout(request):
    if 'username' in request.session:
        del request.session['email']
        del request.session['username']

    return redirect('index')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        print(email, password, name)
        user = Users.objects.filter(email = email)
        if user:
            return render(request, 'signup.html', {'message':True})
        else:
            user = Users(email=email,password=password,name=name)
            user.save()
            return redirect('login')
    return render(request, 'signup.html', {})