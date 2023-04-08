from django.contrib import admin
from walletApp.models import Statement

class StatementAdmin(admin.ModelAdmin):
    list_display = ["name", "amount", "category"]
    list_per_page = 10
    list_editable = ["amount", "category"]
    list_filter = ["category", "amount"]
    search_fields = ["name"]
    fields = ["category", "name", "amount"]

# Register your models here.
admin.site.register(Statement, StatementAdmin)