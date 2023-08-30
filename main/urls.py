from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunoView, name='aluno-lista'),
    #*15
    path('alunoID/<int:id>', views.alunoIDview, name='aluno-detalhe'),


]

