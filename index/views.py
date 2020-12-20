from django.shortcuts import render

# Create your views here.
def index(request):
    if 'username' in request.session:
        username = request.session['username']
    else:
        username = ""
    return render(request, 'index.html', {'username': username})