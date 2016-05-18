# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from bridge import views

urlpatterns = [
    url(r'^deducciones/banco/(?P<affiliate>\d+)$',
        views.DeduccionBancariaAffiliateListView.as_view(),
        name='bridge-affiliate-deduccion-bancaria'),

    url(r'^deducciones/banco/(?P<pk>\d+)/delete$',
        views.DeduccionBancariaDeleteView.as_view(),
        name='bridge-affiliate-deduccion-bancaria-delete'),

    url(r'^deducciones/banco/(?P<pk>\d+)/edit$',
        views.DeduccionBancariaUpdateView.as_view(),
        name='bridge-affiliate-deduccion-bancaria-edit'),
]
