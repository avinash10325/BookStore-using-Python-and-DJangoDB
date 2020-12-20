from django.shortcuts import render, redirect
from store.models import Books
from cart.models import Orders
from contactus.models import Messages
# Create your views here.
def adminpannel(request):
    if 'admin' in request.session:

        queryset1 = Books.objects.all()
        queryset2 = Orders.objects.filter(confirmation = 1)
        queryset3 = Messages.objects.all()
        if request.method == 'POST':
            title = request.POST.get('title')
            price = request.POST.get('price')
            author = request.POST.get('author')
            stock = request.POST.get('stock')
            if request.POST.get('book_id') == '':
                print("add")

                book = Books(title =title, author = author, price = price)
                book.save()
            else:
                print("update")
                Books.objects.filter(Book_id = request.POST.get('book_id')).update(title = title, author=author, price=price, stock=stock)

        return render(request, 'adminpannel.html',{'books':queryset1, 'orders':queryset2, 'messages': queryset3})
    else:
        return redirect('adminlogin')

def remove(request, book_id):
    print(book_id)
    order = Orders
    #order.objects.filter(book_id= book_id, confirmation = 0).delete()

    #Books.objects.filter(Book_id=book_id).delete()
    return redirect('adminpannel')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        if username == 'admin' and password == '12345':
            request.session['admin'] = 'True'
            return redirect('adminpannel')
        else:
            return redirect('adminlogin')

    return render(request, 'adminlogin.html', {})

def adminlogout(request):
    del request.session['admin']
    return redirect('index')