from django.forms.models import BaseModelForm
from .models import Aluno
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

#*15
def alunoView(request):
    alunos_list = Aluno.objects.all()
    return render(request, 'main/alunos.html', {'alunos_list':alunos_list})
#*15

def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    print(aluno)
    return render(request, 'main/alunoID.html', {'aluno':aluno})
#*15
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import AlunoForm

class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm
    success_url = reverse_lazy('aluno-lista')
    template_name = 'main/aluno_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edits import CreateView, UpdateView 
from .forms import AlunoForm
class AlunoCreateView(CreateView):
    model = Aluno 
    form_clss = AlunoForm
    success_url = reverse_lazy('aluno-lista')
    template_name = 'main/aluno_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
#*20
class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'main/aluno_form.html'
    success_url = reverse_lazy('aluno-lista')

#*20

    