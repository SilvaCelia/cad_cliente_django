from django.shortcuts import render
from .models import Cliente
#criar uma função com parametro request(solicitação)


def home (request):
    return render(request,'clientes/home.html')

def clientes(request):
    #Salvar os dados da tela para o banco de dados 
    novo_cliente = Cliente()
    novo_cliente.nome = request.POST.get('nome')
    novo_cliente.idade = request.POST.get('idade')
    novo_cliente.email = request.POST.get('email')
    novo_cliente.save()
    #exibir todos os usuarios já cadastrados em uma nova página
    clientes = {
        'clientes': Cliente.objects.all()
        }
    #Retornar os dados para a pagina de listagem de usuarios
    return render(request,'clientes/clientes.html',clientes)