from django.urls import path
from book1.models import Book 
from book1.views import BookUpdate, BookCreate, BookDelete, BookDetail, BookRetrive, BookTemplate,BookRedirect

app_name = 'book1'  
urlpatterns = [  
path("book-create/", BookCreate.as_view(), name= "BookCreate"),
path("book-retrive/", BookRetrive.as_view(), name= "BookRetrive"),
path("book-detail/<int:pk>", BookDetail.as_view(), name= "BookDetail"),
path("book-update/<int:pk>", BookUpdate.as_view(), name= "BookUpdate"),
path("book-delete/<int:pk>", BookDelete.as_view(), name= "BookDelete"),


path("BookTemplate/", BookTemplate.as_view(), name = "BookTemplate"),
path("BookRedirect/", BookRedirect.as_view(), name = "BookRedirect"),

]