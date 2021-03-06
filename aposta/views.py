from django.shortcuts import render, get_object_or_404
from .models import Concurso, Aposta, Conta
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.utils import timezone

def aposta(request):
    apostas = Aposta.objects.all()
    template = loader.get_template('aposta/index.html')
    context = {'apostas': apostas}
    return render(request, 'aposta/index.html', context)

def detalhe(request, aposta_id):
    aposta = get_object_or_404(Aposta, pk=aposta_id)
    return render(request, 'aposta/detalhe.html', {'aposta': aposta})

def novaaposta(request):
    return render(request, 'aposta/novaaposta.html')

def gravaAposta(request,concurso_id):
    concurso = get_object_or_404(Concurso,pk=concurso_id)
    texto=request.POST['aposta']
    concurso.op
    a=Aposta(concurso,dataAposta=timezone.now(),nome=texto)
    a.save()
    return HttpResponseRedirect(reverse('aposta:index'))
