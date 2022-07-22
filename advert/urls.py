from django.contrib import admin
from django.urls import path,include
from . import views# şu anki klasörden viewi ekle

app_name="advert"

urlpatterns = [
    path('dashboard/', views.dashboard,name="dashboard"),
    path("addadvert/",views.addAdvert,name="addadvert"),
    path("update/<int:id>",views.updateAdvert,name="update"),
    path("delete/<int:id>",views.deleteAdvert,name="delete"),
    path("advert/<int:id>",views.detail,name="detail"),
    path("",views.adverts,name="adverts")
    

]