from django.db import models

class Paciente(models.Model):
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    
    nome_completo = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    condicao_medica = models.TextField()
    medicamentos = models.TextField()
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo
