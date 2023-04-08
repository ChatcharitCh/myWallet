from django.contrib import admin
from walletApp.models import Statement

class StatementAdmin(admin.ModelAdmin):
    list_display = ["name", "amount", "category"]

# Register your models here.
admin.site.register(Statement, StatementAdmin)