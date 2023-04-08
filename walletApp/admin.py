from django.contrib import admin
from walletApp.models import Statement

class StatementAdmin(admin.ModelAdmin):
    list_display = ["name", "amount", "category"]
    list_per_page = 10
    list_editable = ["amount", "category"]

# Register your models here.
admin.site.register(Statement, StatementAdmin)