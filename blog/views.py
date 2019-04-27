from django.http import Http404
from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm

def blog_post_detail_page(request,slug):
	obj=get_object_or_404(BlogPost,slug=slug)
	#qs=BlogPost.objects.filter(slug=slug)
	#if qs.count()==0:
	#	raise Http404
	#obj=qs.first()
	template_name="blog/detail.html"
	context={'obj':obj}
	return render(request,template_name,context)




def blog_post_list_view(request):
	obj=BlogPost.objects.all()
	template_name="blog/list.html"
	context={'obj':obj}
	return render(request,template_name,context)


def blog_post_create_view(request):
	form=BlogPostModelForm(request.POST or None)
	if form.is_valid():
		#obj=BlogPost.objects.create(**form.cleaned_data)
		obj=form.save(commit=False)
		#obj.title=form.cleaned_data['title']+'0'
		obj.save()
		form=BlogPostModelForm()
	template_name="blog/create.html"
	context={'form':form}
	return render(request,template_name,context)

def blog_post_detail_view(request,slug):
	obj=BlogPost.objects.filter(slug=slug)
	template_name="blog/detail.html"
	context={'obj':obj.first()}
	return render(request,template_name,context)

def blog_post_retreive_view(request):
	template_name="blog/retrieve.html"
	context={}
	return render(request,template_name,context)

def blog_post_update_view(request,slug):
	obj=get_object_or_404(BlogPost,slug=slug)
	template_name="blog/update.html"
	context={'object':obj,'form':None}
	return render(request,template_name,context)

def blog_post_delete_view(request):
	template_name="blog/delete.html"
	context={}
	return render(request,template_name,context)