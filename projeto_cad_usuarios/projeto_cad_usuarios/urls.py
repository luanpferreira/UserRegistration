from django.urls import path
from app import views

urlpatterns = [
    # rota, view responsável, nome da referencia
    # usuarios.com
    path('', views.home, name='home'),
    # usuarios.com/usuarios
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
