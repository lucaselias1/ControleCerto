from django.db import models


class Transaction(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Relaciona a transação com um usuário específico
    description = models.CharField(max_length=255)
    # define os campos do modelo de transação
    TRANSACTION_TYPES = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    )
    # definindo categorias iniciais
    CATEGORY_CHOICES = (
        ('alimentacao', 'Alimentação'),
        ('salario', 'Salário'),
        ('lazer', 'Lazer'),
        ('transporte', 'Transporte'),
        ('moradia', 'Moradia'),
        ('saude', 'Saúde'),
        ('educacao', 'Educação'),
        ('outros', 'Outros'),
    )
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField()

    def __str__(self):
        return f"{self.description} - R${self.amount} ({self.transaction_type})"


    


