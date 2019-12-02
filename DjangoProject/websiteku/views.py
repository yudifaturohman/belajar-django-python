from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'index.html')
	
def profil(request):
	return HttpResponse('<h1>Ini halaman profil</h1>')