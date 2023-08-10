from django.db import models
#objetos python que representam as tabelas do banco de dados 

class Cliente(models.Model): #tabela cliente irá herdar da class models.model 

    id_cliente = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    email = models.TextField(max_length=100)
    



