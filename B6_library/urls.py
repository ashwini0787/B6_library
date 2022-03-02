"""B6_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from book1 import views
from django.urls.conf import include 

print( "in urls.py")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("homepage/", views.homepage, name = "homepage"),
    path("show-books/", views.show_books, name = "show-books" ),
    path("edit-books/<int:id>", views.edit_books, name = "edit-books" ),
    path("delete-book/<int:id>", views.delete_books, name = "delete-books"),
    path ("soft-delete<int:id>/", views.soft_delete, name= "soft_delete"),
    path ("inactive-books/", views.inactive_books, name= "inactive_books"),
    path ("restore-books/<int:id>", views.restore_books, name= "restore_books"),
    path ("delete-all-books", views.delete_all_books, name= "delete_all_books"),

    path("form-view",views.form_view, name = "form_view"),
    path("homepage_cbv/",views.homepage_cbv.as_view(name= "ABC"), name = "homepage_cbv"),
    
   path('', include(('book1.urls'), namespace='book1')) 

]

from django.conf.urls import url
from book1 import views

urlpatterns += [
    url(r'^aaa$', views.view_a, name='view_a'),
    url(r'^bbb$', views.view_b, name='view_b'),
    url(r'^ccc$', views.view_c, name='view_c'),
    url(r'^ddd$', views.view_d, name='view_d'),
]
