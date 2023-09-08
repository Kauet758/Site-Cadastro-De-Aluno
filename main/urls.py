from django.urls import path
from .import views
from.views import AlunoCreateView, AlunoUpdateView
urlpatterns = [
    path('', views.alunoView, name='aluno-lista'),
    #*15
    path('alunoID/<int:id>', views.alunoIDview, name='aluno-detalhe'),
    #*15
    path('aluno/create/', AlunoCreateView.as_view(), name='aluno-create'),
    path('aluno/int:pk>/update/', AlunoUpdateView.as_view(), name='aluno-update'),


]

