from django import forms
from django.db import models

# Create your models here.
# SYS_CHOICES = [(str(n), None) for n in range(2, 37)]


class MathExp(models.Model):
    # class SysChoices(models.TextChoices):
    #     BINARY = '2', 'Двоичная'
    #     TERNARY = '3', 'Троичная'
    #     OCTAL = '8', 'Восьмеричная'
    #     DECIMAL = '10', 'Десятичная'
    #     HEXADECIMAL = '16', 'Шестнадцатеричная'
    #     OTHER = '-', 'Другая'
    # initial_sys = models.CharField(default=SysChoices.DECIMAL, choices=SysChoices.choices, max_length=2)
    # next_sys = models.CharField(default=SysChoices.BINARY, choices=SysChoices.choices, max_length=2)


    # isRight = models.CharField(max_length=1, default='1', editable=False)
    initial_num = models.CharField(max_length=50, default='0')
    initial_ss = models.IntegerField(default=0)
    next_ss = models.IntegerField(default=0)
    next_num = models.CharField(max_length=50, default='0')
    dt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.initial_num + '=' + self.next_num

    class Meta:
        verbose_name = 'пример'
        verbose_name_plural = 'примеры'

# class CalcForm(forms.ModelForm):
#     class Meta:
#         model = MathExp
#         fields = '__all__' # or maybe list of poles
        # exclude = [what poles exclude]

# {'isRight': True, 'initial_num': 'ABC36', 'initial_sys': '16', 'next_sys': '10'}