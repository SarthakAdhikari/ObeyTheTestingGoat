from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(self):
    return render(self, 'home.html')
