from django.apps import AppConfig


# this app for report messages to telegram bot
class ReportConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'report'

