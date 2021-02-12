from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enquete/<int:pergunta_id>/', views.detalhar, name='detalhar'),
    path('enquete/<int:pergunta_id>/vote/', views.vote, name='vote'),
    path('oi/', views.oi, name='oi'),
    path('sucesso/', views.sucesso, name='sucesso'),
]