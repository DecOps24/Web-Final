from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello")


def home_page(request):
    return render(request,"index.html")

def about_us(request):
    """ about us page view """
    return render(request, "about_us.html")
