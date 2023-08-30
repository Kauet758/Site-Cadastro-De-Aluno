class AlunoForm(forms.ModelsForm):
    telefone = forms.CharField(widget=forms.TextInput(attrs={'minlenght':'15', 'maxlength':'15', 'onkeyup': 'handlePhone(event)'}))
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
        attrs={'type':'date'}
        )
    )
    class Meta:
        model =Aluno
        fields = ['nome', 'telefone', 'email', 'data_nascimento', 'description']
   
    def _init_(self, *args, **kwargs):
       super()._init_(*args, **kwargs)
       self.fields['nome'].widget.attrs.update({'class':'form-control'})
       self.fileds['telefone'].widget.attrs.update({'class':'form-control'})
       self.fields['email'].widget.attrs.update({'class':'form-control'})
       self.fields['data_nascimento'].widget.attrs.update({'class':'form-control'})
       self.fields['description'].widget.attrs.update({'class':'form-control'})