from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Advert(models.Model):
    #auth.user a atıfta bulunmak, bu alanımız user tablosuna işaret ediyor, o user silindiğinde ona ait tablolar da silinir
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="ilan sahibi")#verbose_name admin kontrol panelinde gözükecek isim
    title=models.CharField(max_length=50,verbose_name="ilan başlığı")
    content=RichTextField()#ck editor RichTextField() # TextField yapılırsa adminde sıkıntı çıkarmıyor
    created_date=models.DateTimeField(auto_now_add=True)
    price=models.CharField(max_length=50,verbose_name="ilan fiyatı")
    marka=models.CharField(max_length=50,verbose_name="ilan markası")
    model=models.CharField(max_length=50,verbose_name="ilan modeli")
    advert_image=models.FileField(blank=True,null=True,verbose_name="ilana resim ekleyin")#bu alan hem boş olabilir hem null olabilir

    def __str__(self):# admin kontrol panelinde Advert object (1) yerine gözükecek isim
        return self.title

    
