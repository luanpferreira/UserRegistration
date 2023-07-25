from django.shortcuts import render
from .models import Usuarios

# Create your views here.
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    # Salva os dados de users inseridos na tela para o banco
    novo_usuario = Usuarios()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Exibe users já cadastrados
    usuarios = {
        'usuarios': Usuarios.objects.all()
    }
    # Retornar para a página
    return render(request, 'usuarios/usuarios.html', usuarios)

