from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    context = {
        'variable': "This variabl in views"
    }
    # return HttpResponse("this is home Page of the company")
    return render(request, 'index.html', context)


def about(request):
    return HttpResponse("This is about page")


def services(request):
    return HttpResponse("This is services")


def contact(request):
    return HttpResponse("Contact through via our email salman@gmail.com")
