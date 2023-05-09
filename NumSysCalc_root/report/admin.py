from django.contrib import admin
from .models import TelegramSettings, Appeal, Coment

class ComentAdm(admin.StackedInline):
    model = Coment
    fields = ('to_phone', 'dt', 'text')
    readonly_fields = ('dt', 'text')
    extra = 0

class AppealAdm(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name', 'phone')

    list_per_page = 5
    list_max_show_all = 100

    inlines = [ComentAdm,]

# Register your models here.
admin.site.register(TelegramSettings)
admin.site.register(Appeal, AppealAdm)
admin.site.register(Coment)
