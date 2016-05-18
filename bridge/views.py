# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.base import ContextMixin, View
from django.views.generic.edit import FormMixin, DeleteView, UpdateView
from django.views.generic.list import ListView

from bridge.forms import DeduccionBancariaForm
from bridge.models import Affiliate, DeduccionBancaria


class AffiliateMixin(ContextMixin, View):
    """
    Adds an :class:`Affiliate` to the child views
    """

    def dispatch(self, *args, **kwargs):
        self.affiliate = get_object_or_404(Affiliate, pk=kwargs['affiliate'])
        return super(AffiliateMixin, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AffiliateMixin, self).get_context_data(**kwargs)
        context['affiliate'] = self.affiliate
        return context


class AffiliateFormMixin(AffiliateMixin, FormMixin):
    """
    Adds a :class:`Affiliate` instance to a form
    """


class DeduccionBancariaAffiliateListView(LoginRequiredMixin, AffiliateMixin,
                                         ListView):
    """
    Displays a list of :class:`DeduccionBancaria` that correspond to a
    :class:`Affiliate`
    """
    model = DeduccionBancaria

    def get_queryset(self):
        return DeduccionBancaria.objects.select_related(
            'banco',
            'account',
            'afiliado',
        ).filter(
            afiliado=self.affiliate
        )


class DeduccionBancariaDeleteView(LoginRequiredMixin, DeleteView):
    """
    Allows deletion of a :class:`DeduccionBancaria`
    """
    model = DeduccionBancaria

    def get_object(self, queryset=None):
        obj = super(DeduccionBancariaDeleteView, self).get_object(queryset)
        self.affiliate = obj.afiliado
        return obj

    def get_success_url(self):
        return reverse(
            'bridge-affiliate-deduccion-bancaria',
            args=[self.affiliate.id]
        )


class DeduccionBancariaUpdateView(LoginRequiredMixin, UpdateView):
    """
    Allows editing :class:`DeduccionBancaria` from the UI
    """
    model = DeduccionBancaria
    form_class = DeduccionBancariaForm
