
import traceback
from django.http import HttpResponse
from django.shortcuts import redirect, render
from book1.models import Book

# Create your views here.
print( "in views.py")
import logging
logger = logging.getLogger("Book")

def homepage(request):
    """Enter Book information"""
    # print(request.method) # GET OR POST
    # print(requset.GET) # queryDict{}
    # print(request.POST) # data which we have entered from frontend in queryDict means dict form 
    logger.info("in homepage ")
    if request.method == "POST":
        # print(dir(request))
        logger.info(f"{request.build_absolute_uri()}......method")
        if not request.POST.get("bid"):
            book_name = request.POST.get("bname")
            book_price = request.POST.get("bprice")
            book_qty = request.POST.get("bqty")
            Book.objects.create(name = book_name, price = book_price, quantity = book_qty)
            return redirect ("homepage")
        else:
            bid = request.POST.get("bid")
            try:
                book_obj = Book.objects.get(id = bid)
            except Book.DoesNotExist as err_msg:
                print(err_msg)
            book_obj.name = request.POST.get("bname")
            book_obj.price = request.POST.get("bprice")
            book_obj.quantity = request.POST.get("bqty")
            book_obj.save()
            return redirect("show-books")

    elif request.method == "GET":
        # print(dir(request))
        all_books = Book.objects.all()       
        return render (request, "home.html", {"Books":all_books})

    
def show_books(request):
    """Show all active books information"""
    all_books = Book.objects.all()
    # print(all_books)
    logger.info("In show Book ")
    return render (request, "show_books.html", {"Books":all_books})


def edit_books(request,id):
    """Edit the information of any book """
    single_book = Book.objects.get(id = id)
    return render (request, "home.html", {"single_book": single_book})

def delete_books(request, id):
    """delete the specific book from UI as well as database"""
    try:
        single_book = Book.objects.get(id = id)
        # print(single_book)
        single_book.delete()
    except  Book.DoesNotExist as err_msg:
        return f"This Id No {id} Does not exit"
      
    return redirect ("show-books")

def soft_delete(request, id):
    """delete the book from UI not form database"""
    single_book = Book.objects.get(id = id)
    single_book.is_active = 0
    single_book.save()
    return redirect ("inactive_books")

def active_books(request):
    '''show all active books'''
    active_books = Book.objects.filter(is_active = 1)
    return render (request, "show-books.html", {"active_books": active_books})


def inactive_books(request):
    """show all inactive book"""
    inactive_books = Book.objects.filter(is_active = 0)
    return render (request, "in-active-books.html", {"inactive_books": inactive_books})

def restore_books(request,id):
    """restore all the inactive book"""
    single_book = Book.objects.get(id = id)
    single_book.is_active = 1
    single_book.save()
    return redirect ("show-books")

def delete_all_books(request):
    """delete all books from UI as well database"""
    all_books = Book.objects.all()
    all_books.delete()
    return redirect ("homepage")
