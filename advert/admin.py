from django.contrib import admin
from .models import Advert


# Register your models here.


#admin.site.register(Advert)

@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):#admin panelini özelleştirmek için
    class Meta:
        model=Advert

    list_display=["title","author","created_date"]#listelenirken hangi özellikleri gösterilsin

    list_display_links=["title","created_date"]#bunlara tıklarsan ilan detayına gidersin

    list_filter=["created_date"]# created_date'e göre verileri listeler


