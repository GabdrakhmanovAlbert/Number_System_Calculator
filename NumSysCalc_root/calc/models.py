# from django import forms
from django.db import models

# Create your models here.
# SYS_CHOICES = [(str(n), None) for n in range(2, 37)]

#!!
class MathExp(models.Model):
    express = models.CharField(max_length=50, default='0')
    res = models.CharField(max_length=25, default='0')
    dt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.express}={self.res}'
    
    class Meta:
        verbose_name = 'пример'
        verbose_name_plural = 'примеры'

class NumSysExp(models.Model):
    initial_num = models.CharField(max_length=50, default='0')
    initial_ss = models.IntegerField(default=0)
    next_ss = models.IntegerField(default=0)
    next_num = models.CharField(max_length=50, default='0')
    dt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.initial_num + '=' + self.next_num

    class Meta:
        verbose_name = 'пример систем счисления'
        verbose_name_plural = 'примеры систем счисления'

# class CalcForm(forms.ModelForm):
#     class Meta:
#         model = MathExp
#         fields = '__all__' # or maybe list of poles
        # exclude = [what poles exclude]

# {'isRight': True, 'initial_num': 'ABC36', 'initial_sys': '16', 'next_sys': '10'}