from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def about_us(request):
    """ about us page view """
    return render(request, "about_us.html")

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        #write logic to save content on an excel sheet
        print(f"New Connection: {name} - {email}") 

        messages.success(request, "Connection established. Our architects will reach out shortly.")
        return redirect('about_us')
    
    return redirect('about_us')
