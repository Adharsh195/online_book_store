from django.shortcuts import render,redirect
from.forms import *
from .models import *
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("welcome")

def add_book(request):
    form=Bookform()
    if request.method=='POST':
        form=Bookform(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            author=form.cleaned_data['author']
            category=form.cleaned_data['category']
            price=form.cleaned_data['price']
            description=form.cleaned_data['description']
            print(title,author,category,price,description)
    return render (request,'add_book.html',{'form':form})



def book_list(request):
    books=Book.objects.all()
    return render (request,'book_list.html',{'books':books})

def category_list(request):
    cat=Category.objects.all()
    return render(request,'category_list.html',{'cat':cat})

def add_category(request):
    if request.method=='POST':
        form=Categoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            form=Categoryform()
            return render (request,'add_category.html',{'form':form})

def edit_book(request, id): 
    book = Book.objects.get(id=id)  #to get only content of id
    if request.method == 'POST': 
        form = Bookform(request.POST) 
        if form.is_valid(): 
            book.title = form.cleaned_data['title']
            book.author = form.cleaned_data['author']
            book.category = form.cleaned_data['category']
            book.price = form.cleaned_data['price']
            book.description = form.cleaned_data['description']
            book.save()
            return redirect('book_list')
    else: 
        form = Bookform(initial={
            'title': book.title,
            'author': book.author,
            'category': book.category,
            'price': book.price,
            'description': book.description
        })

    return render(request, 'edit_book.html', {'form': form}) 

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('book_list')

def edit_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        form = Categoryform(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = Categoryform(instance=category)
    return render(request, 'edit_category.html', {'form': form})

def delete_category(request,id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('category_list')