from django.shortcuts import render,HttpResponse,get_object_or_404
from . import models
# Create your views here.
def post_create(request):
    return render(request,'index.html',{})

def post_detail(request,pk):
    object = get_object_or_404(models.Post,pk=pk)
    context = {'post':object}
    return render(request,'post_detail.html',context)

def post_list(request):
    queryset = models.Post.objects.all()
    #instance = get_object_or_404(models.Post,title='abc')
    context = {'post_list':queryset}
    return render(request,'index.html',context)

def post_update(request):
    return HttpResponse('ma')

def post_delete(request):
    return HttpResponse('ma')