from django.shortcuts import render,redirect
from .models import Books
from cart.models import Orders
from django.db.models import Q
# Create your views here.
def store(request):
    books = Books
    queryset = books.objects.exclude(stock = 0)
    print(queryset)
    if 'username' in request.session:
        username = request.session['username']
    else:
        username = ""
    return render(request, 'store.html', {'query': queryset , 'username':username})

def purchase(request, id):

    print("purhcase",int(id))

    if 'username' in request.session:
        print(request.session['email'])
        book_id = id
        email = request.session['email']
        temp = Books.objects.get(Book_id = book_id)
        order = Orders(book_id=book_id, email=email, price = temp.price)
        order.save()

        temp = Books.objects.get(Book_id=book_id)
        stock = temp.stock - 1

        #book = Books.objects.filter(Book_id=book_id)
        #book.update(stock=stock)
        return redirect('cart')
    else:
        return redirect('login')
