from django.shortcuts import render
from .forms import text1
from .models import text123,comment1
from django.http import HttpResponse
def viewdarkness(request):
    return render(request,'index.html')
# Create your views here.
def fun(request):
    return render(request,'style-demo.html')
def fun1(request):
    return render(request,'full-width.html')
def fun2(request):
    return render(request,'logout.html')
def fun3(request):
    return render(request,'registration.html')
def fun4(request):
    return render(request,'login.html')
def texteditor(request):
    return render(request,'Texteditor.html')
def createpost(request):

    form=text1()
    return render(request,'Texteditor.html',{'form':form})

def blog(request):
    if request.method== 'POST':
        name=request.POST['blog_name']
        obj=text123(text=name)
        obj.save()
        posts=text123.objects.last()
        args={'posts':posts}
        return render(request,'displaying_data.html',args)
def c1(request):
    if request.method=='POST':
        name1=request.POST['comments']
        obj1=comment1(text=name1)
        obj1.save()
        posts = text123.objects.last()
        args = {'posts': posts}
        posts1=comment1.objects.last()
        args1={'posts1':posts1}
        return render(request,'showall.html',args)




