from django.template import loader
from .models import Pergunta, Opcao
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    template = loader.get_template('index_enquete.html')
    perguntas = Pergunta.objects.all()
    contexto = {'perguntas' : perguntas}
    return HttpResponse(template.render(contexto, request))


def oi(request):
    return HttpResponse("Oi galera na view OI.")


def sucesso(request):
    return HttpResponse("flw vlw.")

def detalhar(request, pergunta_id):
    try:
        pergunta = Pergunta.objects.get(id=pergunta_id)
        template = loader.get_template('detalhar.html')
        contexto = {'pergunta' : pergunta}
    except Pergunta.DoesNotExist:
         raise Http404("Pergunta 404")
    return HttpResponse(template.render(contexto, request))

def vote(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        opcao_selecionada = pergunta.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        return render(request, 'detalhar.html', {
            'pergunta': pergunta,
            'error_message': "You didn't select a choice.",
        })
    else:
        opcao_selecionada.votos += 1
        opcao_selecionada.save()
        return render(request, 'detalhar.html', {
            'pergunta': pergunta,
            'error_message': "Voto computado com sucesso",
        })