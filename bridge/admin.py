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
    list_display = ['year', 'month', 'amount', 'inprema', 'inprema_compliment',
                    'amount_compliment', 'alternate']
    search_fields = ['year', 'month']
    ordering = ['year', 'month']


class DeducedAdmin(admin.ModelAdmin):
    list_display = ['affiliate', 'account', 'cotizacion', 'year', 'month',
                    'amount']
    search_fields = ['affiliate__id', ]
    ordering = ['affiliate_id', 'account_id', 'year', 'month']

    def get_queryset(self, request):
        return super(DeducedAdmin, self).get_queryset(request).select_related(
                'affiliate',
                'account',
                'cotizacion'
        )


class DeduccionBancariaAdmin(admin.ModelAdmin):
    list_display = ['afiliado', 'account', 'banco', 'year', 'month',
                    'amount']
    search_fields = ['afiliado__id', ]
    ordering = ['afiliado_id', 'account_id', 'year', 'month']

    def get_queryset(self, request):
        return super(DeduccionBancariaAdmin, self).get_queryset(request).select_related(
                'affiliate',
                'account',
                'banco'
        )


admin.site.register(models.BankReport, BankReportAdmin)
admin.site.register(models.BankAccount, BankAccountAdmin)
admin.site.register(models.Obligation, ObligationAdmin)
admin.site.register(models.Deduced, DeducedAdmin)
admin.site.register(models.DeduccionBancaria, DeduccionBancariaAdmin)
