from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Transaction
from .forms import TransactionForm
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm

@login_required
def dashboard(request):
    # 1. Trata o formulário primeiro
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user  # Vincula ao usuário logado
            transaction.save()
            messages.success(request, 'Transação adicionada com sucesso!')
            return redirect('dashboard')
    else:
        # Se for um acesso via GET (abrir a página), cria um formulário vazio
        form = TransactionForm()

    # 2. Busca os dados filtrados pelo usuário
    transacoes = Transaction.objects.filter(user=request.user).order_by('-date')

    # 3. Cálculos de Saldo
    total_entrada = transacoes.filter(transaction_type='entrada').aggregate(Sum('amount'))['amount__sum'] or 0
    total_saida = transacoes.filter(transaction_type='saida').aggregate(Sum('amount'))['amount__sum'] or 0
    saldo = total_entrada - total_saida

    # 4. Dados para o gráfico (agrupados por categoria)
    categorias_saida = transacoes.filter(transaction_type='saida').values('category').annotate(total=Sum('amount'))

    context = {
        'form': form, # Agora o form SEMPRE existirá aqui
        'transacoes': transacoes,
        'total_entrada': total_entrada,
        'total_saida': total_saida,
        'saldo': saldo,
        'categorias_saida': categorias_saida,
    }

    return render(request, 'transactions/dashboard.html', context)

def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    transaction.delete()
    messages.success(request, 'Transação deletada com sucesso!')
    return redirect('dashboard')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Faça login para continuar.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})