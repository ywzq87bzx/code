from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Book

# Create your views here.

def list_view(request):
    books=Book.objects.all()
    return render(request,'bookstore/list_book.html',locals())

def add_view(request):
    if request.method=='GET':
        return render(request,'bookstore/add_book.html')
    elif request.method=='POST':
        title=request.POST['title']
        price=request.POST['price']
        market_price=request.POST['market_price']
        pub=request.POST['pub']

        Book.objects.create(title=title,price=price,market_price=market_price,pub=pub)
        return HttpResponseRedirect('/books/')

def update_view(request,bid):
    try:
        book=Book.objects.get(id=bid)
    except Exception as e:
        print('error is %s' %e)
        return HttpResponse('bid is error')
    if request.method=='GET':
        return render(request,'bookstore/update_book.html',locals())
    elif request.method=='POST':
        market_price=request.POST['market_price']
        book.market_price=market_price
        book.save()
        return HttpResponseRedirect('/books/')



def delete_view(request):
    bid=request.GET.get('bid')
    try:
        book=Book.objects.get(id=bid)
        book.delete()
    except Exception as e:
        print('error is %s' % e)
        return HttpResponse('bid is error')
    return HttpResponseRedirect('/books/')



