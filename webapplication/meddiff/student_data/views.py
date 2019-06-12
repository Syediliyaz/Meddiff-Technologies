from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmailForm, DataForm


def index(request):
	#Creating a form with one text box to enter text to translate
	#tu es mignon! --> enter this french code in textbox
	form = DataForm(request.POST or None)
	#form.getvalue('to_translate')
	print("a")
	context = {"form":form}
	template = "home.html" 
	if request.method == 'POST':
		print("AB")
	return render (request, template, context)
	#return HttpResponse(var)
	

def index2(request):
	#Creating a form with one text box to enter text to translate
	#tu es mignon! --> enter this french code in textbox
	form = EmailForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			name = form.cleaned_data['Name']
			roll = form.cleaned_data['Roll']
			age = form.cleaned_data['Age']
			gender = form.cleaned_data['Gender']
			print(name,roll,age,gender)
			f = open("data.txt",'a+') 
			f.write(name+","+roll+","+age+","+gender)
			f.write("\n")
			f.close()
	form = EmailForm()
	context = {"form":form}
	template = "home.html"
	return render (request, template, context)