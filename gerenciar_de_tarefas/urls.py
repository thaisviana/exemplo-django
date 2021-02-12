from django.urls import path
from . import views

urlpatterns = [
    path('arquivos/', views.lista_arquivos, name='lista_arquivos'),
    path('', views.index, name='index'),
    path('processos/', views.lista_processos, name='lista_processos'),
    path('processos/<int:pid>/', views.detalhar_processo, name='processo'),
]