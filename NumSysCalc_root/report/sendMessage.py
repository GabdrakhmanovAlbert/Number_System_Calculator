from datetime import datetime
# import asyncio
import requests
from .models import TelegramSettings, Coment, Appeal


def ctime():
	return datetime.now().strftime('[%d/%m/%Y  %H:%M:%S]') 

def save_person_db(name, phone, mess):
	try:
		p = Appeal.objects.get(phone=phone)
	except Appeal.DoesNotExist:
		p = Appeal.objects.create(name=name, phone=phone)
	Coment.objects.create(to_phone=p, text=mess)

def SendTg(queryDict):
	# configure data
	tg_setts = TelegramSettings.objects.get(pk=1)
	api = 'https://api.telegram.org/bot'
	name = queryDict["name"] if queryDict["name"] else 'Undefined'
	phone = f'{queryDict["phone_0"]}{queryDict["phone_1"]}{queryDict["phone_2"]}'
	message = queryDict["message"]
	text = tg_setts.mess_temlate.format(
		name=name,
		phone=phone,
		message=message
	)
	link = f'{api}{tg_setts.token}/sendMessage'

	# send POST to tg
	try:
		req = requests.post(link, data={
			'chat_id': tg_setts.chat_id,
			'text': text
		})
		save_person_db(name, phone, message)
	except Exception as e:
		print(e)
	finally:
		if req.status_code == 200:
			coment = 'Сообщение успешно отправлено'
		elif req.status_code == 400:
			coment = f'Страница не найдена - {link}'
		elif req.status_code == 500:
			coment = f'Не удаётся получить ответ от {api}'
		else:
			coment = 'Неопознанная ошибка'
		print(f'{ctime()}"POST {link}" {req.status_code} {coment}')
