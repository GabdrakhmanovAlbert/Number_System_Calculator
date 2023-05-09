# from django import forms
from django.db import models

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

