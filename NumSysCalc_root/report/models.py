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

class Appeal(models.Model):
	name = models.CharField(max_length=200, verbose_name='Имя')
	phone = models.CharField(max_length=15, verbose_name='Телефон', unique=True)

	def __str__(self):
		return f'{self.phone}'

	class Meta:
		verbose_name = 'Обращение'
		verbose_name_plural = 'Обращения'

class Coment(models.Model):
	to_phone = models.ForeignKey(Appeal, on_delete=models.CASCADE, to_field='phone', verbose_name='Телефон заявителя')
	text = models.TextField(verbose_name='Текст комментария')
	dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

	def __str__(self):
		return f'{self.text}'

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'