from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hozzad/', views.hozzad, name='hozzad'),
    path('konyvek/', views.konyvek, name='konyvek'),
    path('szerzok/', views.szerzok, name='szerzok'),
    path('adatok/', views.adatok, name='adatok'),
    path('mufajok/', views.mufajok, name='mufajok'),
    path('szerkeszt/<int:pk>/', views.szerkeszt_konyv, name='szerkeszt_konyv'),
    path('torol/<int:konyv_id>/', views.torol_konyv, name='torol_konyv'),


    

]