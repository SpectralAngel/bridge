# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bootstrap3_datetime.widgets import DateTimePicker
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Submit
from django import forms
from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _

from bridge.models import Affiliate, DeduccionBancaria


class FieldSetFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FieldSetFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.html5_required = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-7'
        self.field_names = self.fields.keys()

    def set_legend(self, text):
        self.helper.layout = Fieldset(text, *self.field_names)

    def set_action(self, action):
        self.helper.form_action = action


class FieldSetModelFormMixinNoButton(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FieldSetModelFormMixinNoButton, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.html5_required = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-7'
        self.field_names = self.fields.keys()

    def set_legend(self, text):
        self.helper.layout = Fieldset(text, *self.field_names)

    def set_action(self, action):
        self.helper.form_action = action


class FieldSetModelFormMixin(FieldSetModelFormMixinNoButton):
    def __init__(self, *args, **kwargs):
        super(FieldSetModelFormMixin, self).__init__(*args, **kwargs)
        self.helper.add_input(Submit('submit', _('Guardar')))


class AfiliadoFormMixin(FieldSetModelFormMixin):
    afiliado = forms.ModelChoiceField(
        queryset=Affiliate.objects.all(),
        widget=forms.HiddenInput(),
    )


class DeduccionBancariaForm(AfiliadoFormMixin):
    class Meta:
        model = DeduccionBancaria
        fields = '__all__'

    day = forms.DateField(widget=DateTimePicker(
        options={"format": "YYYY-MM-DD"}),
        label=_('Fecha')
    )

    def __init__(self, *args, **kwargs):
        super(DeduccionBancariaForm, self).__init__(*args, **kwargs)
        self.helper.add_input(
            Submit('submit', _('Formulario de Deduccion Bancaria'))
        )
