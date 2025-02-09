from django.contrib import admin
from django.urls import path
from alkalmazas.views import hozzad, index, konyvek, szerzok, adatok, mufajok, szerkeszt_konyv, torol_konyv  # Javított import
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('hozzad/', hozzad, name='hozzad'),
    path('konyvek/', konyvek, name='konyvek'),
    path('szerzok/', szerzok, name='szerzok'),
    path('adatok/', adatok, name='adatok'),
    path('mufajok/', mufajok, name='mufajok'),
    # Új útvonal hozzáadva a szerkesztéshez
    path('szerkeszt/<int:konyv_id>/', szerkeszt_konyv, name='szerkeszt_konyv'),
    path('torol/<int:konyv_id>/', torol_konyv, name='torol_konyv'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)