from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login
from django.shortcuts import HttpResponse
import logging
logger = logging.getLogger('sistemaVeicular')

class IndexView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, template_name='index.html',context={'nome':'veiculos'})
        else:
            return HttpResponse('Altenticado')
    def post(self, request):
        usuario = request.POST.get('username')
        senha = request.POST.get('senha')
        logger.info(f'Usuário: {usuario}')
        logger.info(f'Senha: {senha}')
        
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Logado')
            return render(request, template_name='index.html',context={'mensagem':'Usuario inativo'})
        return render(request, template_name='index.html',context={'mensagem':'usuario ou senha iinvalidos'})