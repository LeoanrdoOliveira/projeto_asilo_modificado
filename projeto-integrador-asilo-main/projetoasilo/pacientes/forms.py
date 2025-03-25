from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'condicao_medica': forms.Textarea(attrs={'rows': 3}),
            'medicamentos': forms.Textarea(attrs={'rows': 3}),
        }

class ReceitaForm(forms.Form):
    paciente = forms.ModelChoiceField(queryset=Paciente.objects.all(), label="Paciente")
    medico = forms.CharField(max_length=200, label="Nome do Médico")
    crm = forms.CharField(max_length=20, label="CRM do Médico")
    prescricao = forms.CharField(widget=forms.Textarea, label="Prescrição")
    data_receita = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Data da Receita")