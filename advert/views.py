from email import message
from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from django.urls import is_valid_path
from .models import Advert
from .forms import AdvertForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def dashboard(request):
    adverts=Advert.objects.filter(author=request.user)
    context={"adverts":adverts}
    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")#user-urls-login
def addAdvert(request):
    form=AdvertForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        advert=form.save(commit=False)
        advert.author=request.user
        advert.save()

        messages.success(request,"Makale başarıyla oluşturuldu.")
        return redirect("advert:dashboard")#??????????
    
    return render(request,"addadvert.html",{"form":form})



@login_required(login_url="user:login")#user-urls-login
def deleteAdvert(request,id):
    advert=get_object_or_404(Advert,id=id)
    advert.delete()
    messages.success(request,"makale başarıyla silindi")
    return redirect("advert:dashboard")


def detail(request,id):
    advert =get_object_or_404(Advert,id=id)
    return render(request,"detail.html",{"advert":advert})

@login_required(login_url="user:login")#user-urls-login
def updateAdvert(request,id):
    advert=get_object_or_404(Advert,id=id)
    form=AdvertForm(request.POST or None,request.FILES or None,instance=advert)#instance=advert# advert içindeki bilgiler formun içine yazılır

    if form.is_valid():
        advert=form.save(commit=False)
        advert.author=request.user
        advert.save()
        messages.success(request,"Makale başarıyla güncellendi..")
        return redirect("advert:dashboard")#şu uygulamanın altındaki: şu url

    return render(request,"update.html",{"form":form})

def adverts(request):

    keyword =request.GET.get("keyword")

    if keyword:
        adverts=Advert.objects.filter(title__contains=keyword)
        return render(request,"adverts.html",{"adverts":adverts})

    adverts=Advert.objects.all()

    return render(request,"adverts.html",{"adverts":adverts})


