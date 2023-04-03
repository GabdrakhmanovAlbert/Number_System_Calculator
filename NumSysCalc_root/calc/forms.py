from django import forms


# class CalcForm(forms.Form):
# 	calc_textarea = forms.CharField(widget=forms.widgets.Textarea(attrs={
# 		'type': 'text', 'id': 'calc-screen',
# 		'autocomplete': 'off', 'placeholder': 'Enter:',
# 		'rows': '1', 'autofocus': 'autofocus'
# 	}), )
class CalcForm(forms.Form):
	mathExpInput = forms.CharField(min_length=1, max_length=50, required=True, initial='0', widget=forms.Textarea(attrs={'autocomplete': 'off', 'placeholder': 'Enter:', 'rows': '1', 'autofocus': 'autofocus'}))
	mathExp = forms.CharField(initial='0', widget=forms.widgets.HiddenInput())

class NumSysCalcForm(forms.Form):
	isRight = forms.CharField(widget=forms.widgets.HiddenInput(), initial='1')
	calc_input = forms.CharField(max_length=50, min_length=1,
		label='Введите число: ', widget=forms.TextInput(attrs={'autofocus': True})) # , initial='0'
	ss = forms.NullBooleanField(
							label='Его система счисления',
							widget=forms.RadioSelect(
							choices=[
									('2', 'Двоичная'),
									('3', 'Троичная'),
									('8', 'Восьмеричная'),
									('10', 'Десятичная'),
									('16', 'Шестнадцатеричная'),
									('-', 'Другая'),
									],
							)
							)
	other_ss = forms.IntegerField(min_value=2, max_value=36,
	initial=2, label='Какая? (число)', required=False)
	ss1 = forms.NullBooleanField(
							label='Перевести в',
							widget=forms.RadioSelect(
							choices=[
									('2', 'Двоичную'),
									('3', 'Троичную'),
									('8', 'Восьмеричную'),
									('10', 'Десятичную'),
									('16', 'Шестнадцатеричную'),
									('-', 'Другую'),
									],
							)
							)
	other_ss1 = forms.IntegerField(min_value=2, max_value=36,
	initial=2, label='Какую? (число)', required=False)

# {'csrfmiddlewaretoken': ['CvwvsE7qRnmMKD2CnY5IZe0Sv0DFJJvqB4av64n9PhpEtluj54Qx2bHsQSoT60EN'], 'isRight': ['1'], 'calc_input': ['slgjjlkjdfgdl'], 'ss': ['-'], 'other_ss': ['36'], 'ss1': ['-'],'other_ss1': ['2'], 'btn_send': ['']}
#print(f.fields['calc_input'].get_bound_field(f, 'calc_input'))
#<input type="text" name="calc_input" value="0" maxlength="50" minlength="1" required id="id_calc_input">