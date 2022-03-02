from dataclasses import field, fields
from email import message
from msilib.schema import IsolatedComponent
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from B6_library import urls
from book1.forms import  BookForm
from book1.models import Book
from django.contrib import messages

# def form_view(request):
#     context = {"form": studForm()}
#     return render( request, "forms.html", context)



def form_view(request):
    # print(BookForm())  # it gives the Html page
    if request.method == "POST":
        print(request.POST)
        form = BookForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["name"])
            form.save()
            messages.success(request, "data saved succesfully")
            messages.info(request, "redirecting to home page")
        else:
            messages.error(request, "Invalid Http method")
        return redirect("form_view")

    elif request.method == "GET":
        context = {"form": BookForm()}
        return render( request, "forms.html", context)
    else: 
        return HttpResponse("Invalide HTTP method" )

from django.views import View

class homepage_cbv(View):
    name = None
    def get(self, request):
        print ("in get method")
        print(self.name)
        return HttpResponse(" in get")

    def post(self, request):         
        print ("in post method")
        print(request.POST)
        return HttpResponse(" in post")

    def delete(self, request):
        print(" in delete method")
        return HttpResponse("in delete")

    def put(self, request):
        print(" in put")
        return HttpResponse("in put")

    def patch(self, request):
        print("in patch method")
        return HttpResponse(" in patch")

from django.views.generic import TemplateView, RedirectView

class BookTemplate(TemplateView):
    extra_context = {"form": BookForm}
    template_name = "forms.html"

class BookRedirect(RedirectView):
    url = "http://127.0.0.1:8000/homepage_cbv/"    # it need absolute url



from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

class BookCreate(CreateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy ("book1:BookCreate") # imp  Note-------("appname:pagename )because we are making urls.py file under app folder

class BookRetrive(ListView):
    model = Book
   
    
class BookDetail(DetailView):
    model = Book
  
class BookUpdate(UpdateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy ("book1:BookCreate")

class BookDelete(DeleteView):
    model = Book
    fields = "__all__"
    template_name_suffix = '_confirm_delete' 
    success_url = reverse_lazy ("book1:BookCreate")