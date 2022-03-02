from django.http import HttpResponse

def view_c(request):
   return HttpResponse('I am in view_c')

def view_d(request):
    return HttpResponse('I am in view_d')