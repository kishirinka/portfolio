from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aboutme.html')

def project(request):
    return render(request, 'project.html')

def contact(request):  # Add this function
    return render(request, 'contact.html')
