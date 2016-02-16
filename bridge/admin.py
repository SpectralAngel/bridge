from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from bridge.models import BankReport, BankAccount


class BankReportAdmin(admin.ModelAdmin):
    list_display = ['banco', 'year', 'month']
    ordering = ('year', 'month')


class BankAccountAdmin(admin.ModelAdmin):
    list_display = ['bank_report', 'get_month', 'get_year', 'account', 'amount']

    def get_month(self, obj):
        return obj.bank_report.month

    def get_year(self, obj):
        return obj.bank_report.year


admin.site.register(BankReport, BankReportAdmin)
admin.site.register(BankAccount, BankAccountAdmin)
