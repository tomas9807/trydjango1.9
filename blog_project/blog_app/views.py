from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.contrib import messages
from . import models
from .forms import PostForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def post_create(request):
    
    if request.method=='POST':
        form = PostForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,"YOU HAVE SUCCESSFULLY CREATED A POST")
            context = {'form':form}
            
        else:
            messages.success(request,"YOU HAVE SUCCESSFULLY CREATED A POST")
        return redirect('post:home')
    else:
        form = PostForm()
        context = {'form':form,'updating':False}
        return render(request,'post_form.html',context)

def post_detail(request,pk):
    object = get_object_or_404(models.Post,pk=pk)
    context = {'post':object}
    return render(request,'post_detail.html',context)

def post_list(request):
    queryset = models.Post.objects.all()
    paginator = Paginator(queryset,5)
    page = request.GET.get('page')
    query = paginator.get_page(page)
    #instance = get_object_or_404(models.Post,title='abc')
    context = {'post_list':query}
    return render(request,'index.html',context)


def post_update(request,pk=None):
        post = get_object_or_404(models.Post,pk=pk)
        form = PostForm(request.POST or None,request.FILES or None, instance=post)
        context = {'form':form,'updating':True,'pk':pk}
        if form.is_valid():
            post.title = form.cleaned_data.get('title')
            post.content = form.cleaned_data.get('content')
            post.save()

            return redirect('post:home')
        else:
            return render(request,'post_form.html',context)

    

def post_delete(request,pk=None):
    post = get_object_or_404(models.Post,pk=pk)
    post.delete()
    return redirect('post:home')

    