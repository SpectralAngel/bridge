# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from django.utils import timezone

Zero = Decimal()
dot01 = Decimal(0.01)


class PeriodBased(object):
    def period(self, retrasada=False, gracia=False):

        (start, end) = (1, 13)
        now = timezone.now()
        if self.affiliate.joined.year == self.year:
            start = self.affiliate.joined.month

        if self.year == now.year:
            if retrasada:
                end = now.month
            else:
                if gracia:
                    end = now.month - 4
                else:
                    end = now.month + 1
        else:
            if gracia:
                end = 8

        if end <= 0:
            end = 1

        return start, end

    def calculate_amount(self, month):
        """
        Calculates the amount a month has to get payed
        :param month: the month we need the calculation for
        :return: the complete amount
        """
        pass

    def month_payment(self, month, period=None):

        """Muestra la cantidad pagada en el mes especificado"""

        if period is None:
            inicio, fin = self.period()
            period = range(inicio, fin)

        if month not in period:
            return Zero

        if not getattr(self, 'month{0}'.format(month)):
            return Zero

        return self.calculate_amount(month - 1)

    def debt_month(self, month, period=None):

        """Muestra la cantidad debida en el mes especificado"""

        if period is None:
            inicio, fin = self.period()
            period = range(inicio, fin)

        if month not in period:
            return Zero

        if getattr(self, 'month{0}'.format(month)):
            return Zero

        return self.calculate_amount(month - 1)

    def delayed(self):

        if self.affiliate.joined is None:
            return Zero

        """Obtiene el primer mes en el que no se haya efectuado un pago en las
        aportaciones.
        """

        inicio, fin = self.period(retrasada=True)
        for n in range(inicio, fin):
            if not getattr(self, 'month{0}'.format(n)):
                return n

        return Zero

    class Meta:
        managed = False
        db_table = 'cuota_table'
        unique_together = (('affiliate', 'year'),)

    def january(self):
        amount = self.calculate_amount(0)
        if not self.month1:
            return Zero
        return amount

    def february(self):
        amount = self.calculate_amount(1)
        if not self.month2:
            return Zero
        return amount

    def march(self):
        amount = self.calculate_amount(2)
        if not self.month3:
            return Zero
        return amount

    def april(self):
        amount = self.calculate_amount(3)
        if not self.month4:
            return Zero
        return amount

    def may(self):
        amount = self.calculate_amount(4)
        if not self.month5:
            return Zero
        return amount

    def june(self):
        amount = self.calculate_amount(5)
        if not self.month6:
            return Zero
        return amount

    def july(self):
        amount = self.calculate_amount(6)
        if not self.month7:
            return Zero
        return amount

    def august(self):
        amount = self.calculate_amount(7)
        if not self.month8:
            return Zero
        return amount

    def september(self):
        amount = self.calculate_amount(8)
        if not self.month9:
            return Zero
        return amount

    def octuber(self):
        amount = self.calculate_amount(9)
        if not self.month10:
            return Zero
        return amount

    def november(self):
        amount = self.calculate_amount(10)
        if not self.month11:
            return Zero
        return amount

    def december(self):
        amount = self.calculate_amount(11)
        if not self.month12:
            return Zero
        return amount

    def total(self):
        """
        Calulates the total amount that has been payed this year
        :return:
        """
        inicio, fin = self.period()
        period = range(inicio, fin)
        return sum(self.month_payment(month, period) for month in period)

    def debt(self):

        inicio, fin = self.period()
        period = range(inicio, fin)
        return sum(self.debt_month(month, period) for month in period)
