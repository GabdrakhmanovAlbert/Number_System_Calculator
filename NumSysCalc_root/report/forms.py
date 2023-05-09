from django import forms

#forms.TextInput(attrs={'size': code_length, 'maxlength': code_length}),
#forms.TextInput(attrs={'size': num_length, 'maxlength': num_length})

class PhoneWidget(forms.MultiWidget):
	def __init__(self, code_length=3, num_length=7, attrs=None):
		widgets = [
			forms.Select(choices=
									[
									('+7', '+7'), #ru
									('+380', '+380'),  # ukr
									('+49', '+49'),  #ger
									('+33', '+33'),  #fr
									('+33', '+30'),  #grec
									('+93', '+93'),  #afg
									('+374', '+374'),  #arm
									('+99', '+99'),  #azerb
									('+971', '+971'),  #Объединённые арабские эмираты
									('+992', '+992'), #tadjik
									('+998', '+998'),  #uzb
										]),
				forms.TextInput(attrs={'minlength': 1, 'maxlength': code_length}),
				forms.TextInput(attrs={'minlength': 1, 'maxlength': num_length})
				]
		super(PhoneWidget, self).__init__(widgets, attrs)
	
	def decompress(self, value):
		if value:
			return [value.code, value.number]
		else:
			return ['', '']
	
	def format_output(self, rendered_widgets):
		return f'{rendered_widgets[0]}({rendered_widgets[1]})-{rendered_widgets[2]}'

class PhoneField(forms.MultiValueField):
	def __init__(self, code_length=3, num_length=7, *args, **kwargs):
		list_fields = [
					forms.NullBooleanField(),
					forms.CharField(),
					forms.CharField()]
		super(PhoneField, self).__init__(list_fields, widget=PhoneWidget(code_length, num_length), *args, **kwargs)
	
	def compress(self, values):
		return f'{values[0]}{values[1]}{values[2]}'

class ReportForm(forms.Form):
	name = forms.CharField(max_length=200, required=False, label='Ваше имя')
	phone = PhoneField(label='Ваш телефон')
	message = forms.CharField(widget=forms.Textarea(), label='Ваш вопрос или предложение')

