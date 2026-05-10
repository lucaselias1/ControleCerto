from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'transaction_type', 'category', 'date',)
    list_filter = ('transaction_type', 'category', 'date')
    search_fields = ('description',)
    ordering = ('-date',)
    date_hierarchy = 'date'
