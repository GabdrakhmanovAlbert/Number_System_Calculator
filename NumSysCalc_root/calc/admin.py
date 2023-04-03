from django.contrib import admin
from .models import MathExp


class ExpAdm(admin.ModelAdmin):
    list_display = ('initial_num', 'dt')
    readonly_fields = ('initial_num', 'initial_ss', 'next_num', 'next_ss', 'dt')
    fields = ('initial_num', 'initial_ss', 'next_num', 'next_ss', 'dt')

# Register your models here.
admin.site.register(MathExp, ExpAdm)