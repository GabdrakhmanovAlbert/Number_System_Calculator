from django.apps import AppConfig


class CalcConfig(AppConfig):
	default_auto_field = "django.db.models.BigAutoField"
	name = "calc"

#
class TranslaterSS():
	'''
	get QueryDict like this:
		{'csrfmiddlewaretoken': ['NFpBuZiVt5mTyT7SUy0RUgS0JCoZeMSR5sOLM9pKzuacd2Z51n50qupEPJY3fheV'],
		'isRight': ['1'],
		'calc_input': ['101001'],
		'ss': ['2'], 
		'other_ss': ['2'], 
		'ss1': ['10'], 
		'other_ss1': ['2'], 
		'btn-send': ['']}
	and Instance.translateSS() -> '' (str, with num instance.calc_input in instance.ss1)

	'''

	BUILTIN_FUNCS = {2:bin, 8:oct, 16:hex}
	EXTRA_NUMS = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G',
	17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N',
	24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U',
	31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}


	def __init__(self, queryDict):
		self.isRight = queryDict['isRight'][0]
		self.minus = queryDict['calc_input'][0].startswith('-')
		parsed_input = queryDict['calc_input'].replace(',', '.').replace('-', '').split('.')
		if len(parsed_input) == 2:
			self.int, self.float = parsed_input
		elif len(parsed_input) == 1:
			self.int, self.float = parsed_input[0], ''
		else:
			self.isRight = '0'
		self.ss = int(queryDict['other_ss'] if queryDict['ss'] == '-' else queryDict['ss'])
		self.ss1 = int(queryDict['other_ss1'] if queryDict['ss1'] == '-' else queryDict['ss1'])


	@classmethod
	def _convert_2sym_alpha(cls, num: int, ss: int):
		return cls.EXTRA_NUMS.get(num % ss, str(num % ss))

	@classmethod
	def to10_float(cls, num: str, ss: int):
		ss_num = 0
		for i, n in enumerate(num):
			ss_num += int(n, 36) * (ss ** -(i + 1))
		return str(ss_num).replace('.', ',')[1:]

	@classmethod
	def from10_int(cls, num: int, ss: int):
		ss_num = ''
		if num == 0:
			return '0'
		while num:
			ss_num = cls._convert_2sym_alpha(num, ss) + ss_num
			num //= ss
		return ss_num

	@classmethod
	def from10_float(cls, num: str, to_ss: int):
		num = float('0.' + num)
		print(num)
		ss_num = ','
		for _ in range(12):
			num *= to_ss
			extra, num = str(num).split('.')
			ss_num += cls._convert_2sym_alpha(int(extra), to_ss)
			num = float('0.' + num)
			if num == 0:
				break
		return ss_num


	def to10(self):
		int_part = str(int(self.int, self.ss))
		if self.float:
			return (int_part, TranslaterSS.to10_float(self.float, self.ss))
		return (int_part, '')

	def from10(self):
		try:
			int_part = TranslaterSS.BUILTIN_FUNCS[self.ss1](int(self.int))[2:]
		except KeyError:
			int_part = TranslaterSS.from10_int(int(self.int), self.ss1)
		if self.float:
			return (int_part, TranslaterSS.from10_float(self.float, self.ss1))
		return (int_part, '')

	def translateSS(self):
		if not int(self.isRight):
			return ''

		if self.ss1 == 10:
			self.int, self.float = self.to10()
		elif self.ss == 10:
			self.int, self.float = self.from10()
		else:
			self.int, self.float = self.to10()
			self.float = self.float.replace(',', '')
			self.int, self.float = self.from10()
		
		if self.minus:
			self.int = '-' + self.int
		
		if self.float:
			return str(self.int + self.float).upper()
		return str(self.int).upper()


# reshator = TranslaterSS({
# 	'isRight': ['1'],
# 	'calc_input': ['0.562'], 
# 	'ss': ['10'], 
# 	'other_ss': ['2'], 
# 	'ss1': ['3'], 
# 	'other_ss1': ['2']
# })

# print(reshator.translateSS())
