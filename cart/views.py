from django.shortcuts import render, redirect
from .models import Orders
from store.models import Books
# Create your views here.
def cart(request):
    if 'username' in request.session:
        email = request.session['email']
        order = Orders
        queryset = order.objects.filter(email = email, confirmation = 0)
        queryset1 = order.objects.filter(email=email, confirmation= 1)
        print(queryset)
        total = 0
        for i in queryset:
            total = total + i.price
        print(total)
        return render(request, "cart.html", {'query': queryset,'query1': queryset1, 'username': request.session['username'], 'total':total})
    else:
        return redirect('login')

def remove(request, order_id):
    print(order_id,"item removed")
    order = Orders.objects.get(order_id = order_id)
    print(order.order_id)
    order.delete()
    return redirect(cart)

def confirm(request):
    print("order confirmed")
    order = Orders
    book = Books
    email = request.session['email']
    queryset = order.objects.filter(email=email, confirmation = 0)
    l = []
    for i in queryset:
        l.append(i.book_id)
    for i in l:
        query = book.objects.get(Book_id = int(i))
        if int(query.stock) >= 1:
            crnt_stock = int(query.stock) - 1
            book.objects.filter(Book_id = int(i)).update(stock = crnt_stock)
            order.objects.filter(email=email, book_id =i).update(confirmation=1)

        else:
            pass
    order.objects.filter(email = email).update(confirmation = 1)

    return redirect('cart')