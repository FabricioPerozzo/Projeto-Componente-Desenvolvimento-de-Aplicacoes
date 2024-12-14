from django.db import models

class Funcionario(models.Model): 
    nome = models.CharField(max_length=100, null= False, blank=False) 
    cpf = models.DateField(null=False, blank=False) 
    email = models.EmailField(null=False, blank=False) 
    remuneracao = models.CharField(max_length=100, null=False, blank=False)

def __str__(self):
        return self.nome

