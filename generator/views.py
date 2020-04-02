from django.shortcuts import render
from django.http import HttpResponse
import string
import random
# Create your views here.
def home(request):
	return render(request,'generator/home.html',{'password':'vmttto1991'})
def password(request):
	password=''
	characters=list(string.ascii_lowercase)
	length=int(request.GET.get('length',9))
	if length>11:length=11
	if(request.GET.get('uppercase')):
		characters.extend(string.ascii_uppercase)
	if(request.GET.get('number')):
		characters.extend(list('0123456789'))
	if(request.GET.get('special')):
		characters.extend(list('!@#$%^&*()'))

	for i in range(length):
		password+=random.choice(characters)

	return render(request,'generator/password.html',{'password':password})

def about(request):
	return render(request,'generator/about_me.html')	
def eggsshow(request):
	return HttpResponse("<h1>Eggs are show tasty</h1>")