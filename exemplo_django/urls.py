from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('enquete.urls')),
    path('gt/', include('gerenciar_de_tarefas.urls')),
]
