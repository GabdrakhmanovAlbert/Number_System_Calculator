from datetime import datetime

import requests

from .models import TelegramSettings


# POST: <QueryDict: {'csrfmiddlewaretoken': ['Sm892iXOv0bbZag1Rkr2OO0hCceyPW5tHqRzlocEBO8B9fpELRflTpoyxGyKbxRZ'],
# 				   'name': ['Василий'],
# 				   'phone_0': ['+7'],
# 				   'phone_1': ['100'],
# 				   'phone_2': ['1000000'],
# 				   'message': ['дрвп\r\nп\r\nвы\r\nп\r\nвыа\r\nп\r\nп']}>
def ctime():
	return datetime.now().strftime('[%d/%m/%Y  %H:%M:%S]') 


def SendTg(queryDict):
	# configure data
	tg_setts = TelegramSettings.objects.get(pk=1)
	api = 'https://api.telegram.org/bot'
	text = tg_setts.mess_temlate.format(
		name=queryDict["name"] if queryDict["name"] else 'Undefined',
		phone=f'{queryDict["phone_0"]}{queryDict["phone_1"]}{queryDict["phone_2"]}',
		message=queryDict["message"]
	)
	link = f'{api}{tg_setts.token}/sendMessage'

	# send POST to tg
	try:
		req = requests.post(link, data={
			'chat_id': tg_setts.chat_id,
			'text': text
		})
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
