from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro_paciente, name='cadastro_paciente'),
    path('lista/', views.lista_pacientes, name='lista_pacientes'),
    path('receita/', views.gerar_receita, name='gerar_receita'),
    path('remover/<int:paciente_id>/', views.remover_paciente, name='remover_paciente'),
]