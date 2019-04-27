from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm

def home_page(request):
	context={"title":'home'}
	if request.user.is_authenticated:
		context={"title":'home',"list":[1,2,3,4,5]}
	return render(request,"home.html",context);

def about_page(request):
	context={"title":'about'}
	return render(request,"about.html",context);


def contact_page(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form=ContactForm()
	else:
		print('hii')

	template_name='contact.html'
	context={
			"title":'contact',
			"form" : form
			}
	return render(request,template_name,context);



def courses_page(request):
	context={"title":'home'}
	return render(request,"home.html",context);

def example_page(request):
	context={"title":'Example'}
	template_name='home.html'
	template_obj=get_template(template_name)
	render_obj=template_obj.render(context)
	return HttpResponse(render_obj);

