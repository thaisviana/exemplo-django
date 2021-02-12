from django.contrib import admin
from .models import Pergunta, Opcao

class OpcaoInline(admin.TabularInline):
    model = Opcao

@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    inlines = [
        OpcaoInline,
    ]