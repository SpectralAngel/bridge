from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from bridge import models


class BankReportAdmin(admin.ModelAdmin):
    list_display = ['banco', 'year', 'month']
    ordering = ('year', 'month')


class BankAccountAdmin(admin.ModelAdmin):
    list_display = ['bank_report', 'get_month', 'get_year', 'account', 'amount']

    def get_month(self, obj):
        return obj.bank_report.month

    def get_year(self, obj):
        return obj.bank_report.year


class ObligationAdmin(admin.ModelAdmin):
    list_display = ['year', 'month', 'amount', 'inprema', 'amount_compliment',
                    'compliment', 'alternate']
    search_fields = ['year', 'month']
    ordering = ['year', 'month']


class DeducedAdmin(admin.ModelAdmin):
    list_display = ['affiliate_id', 'account' 'year', 'month', 'amount']
    search_fields = ['affiliate__id', ]
    ordering = ['affiliate_id', 'account_id', 'year', 'month']


admin.site.register(models.BankReport, BankReportAdmin)
admin.site.register(models.BankAccount, BankAccountAdmin)
admin.site.register(models.Obligation, ObligationAdmin)
