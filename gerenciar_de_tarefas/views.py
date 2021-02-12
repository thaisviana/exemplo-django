from django.shortcuts import render
from datetime import datetime, timezone
from django.shortcuts import render
import os
import psutil

# Create your views here.

class InfoArquivo():

    def __init__(self,name, atime, mtime):
        self.nome = name
        self.dt_acesso = atime
        self.dt_modificacao = mtime

def lista_arquivos(request):
    lista =  []
    for name in os.listdir('/Users/thaisviana/Downloads'):
        p = f"/Users/thaisviana/Downloads/{name}"
        stat_result = os.stat(p)
        atime = datetime.fromtimestamp(stat_result.st_atime, tz=timezone.utc).strftime('%d/%m/%Y-%H:%M')
        mtime = datetime.fromtimestamp(stat_result.st_mtime, tz=timezone.utc).strftime('%d/%m/%Y-%H:%M')
        info = InfoArquivo(name, atime, mtime)
        lista.append(info)
    contexto = {"lista" : lista}
    return render(request, 'lista_arquivos.html', contexto)

def lista_processos(request):
    procs=[]
    for proc in psutil.process_iter():
        pinfo = proc.as_dict(attrs=['pid', 'name', 'memory_percent', 'cpu_percent'])
        procs.append(pinfo)
    contexto = {"processos" : procs}
    return render(request, 'lista_processos.html', contexto)

def detalhar_processo(request, pid):
    contexto = {"processo" : psutil.Process(pid)}
    return render(request, 'detalhar_processo.html', contexto)

def index(request):
    contexto = {}
    return render(request, 'index.html', contexto)
