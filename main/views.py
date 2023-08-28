from .models import Aluno
from django.http import HttpResponse

def alunoView(request):
    alunos_list = Aluno.objects.all()
    alunos_str = '\n'.join([str(aluno) for aluno in alunos_list])
    return HttpResponse(alunos_str)

# Create your views here.
