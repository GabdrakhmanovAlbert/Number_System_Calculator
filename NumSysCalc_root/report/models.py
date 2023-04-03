from django.db import models

# Create your models here.
class TelegramSettings(models.Model):
	chat_id = models.CharField(max_length=50, verbose_name='id чата')
	token = models.CharField(max_length=75, verbose_name='token бота')
	mess_temlate = models.TextField(verbose_name='Шаблон сообщения')

	def __str__(self):
		return self.chat_id
	
	class Meta:
		verbose_name = 'Настройка'
		verbose_name_plural = 'Настройки'



