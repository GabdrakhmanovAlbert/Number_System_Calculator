from calc.apps import TranslaterSS
from calc.forms import CalcForm, NumSysCalcForm
from calc.models import MathExp
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import redirect, render
from report.forms import ReportForm
from report.sendMessage import SendTg

# views
NumSysRes = ''

def main_page(request):
	global NumSysRes
	if request.POST:
		print("POST:", request.POST)
		nsys_form = NumSysCalcForm(request.POST)
		calc_form = CalcForm(request.POST)
		# rep_form = ReportForm(request.POST)
		print('calc form:', calc_form.is_valid())
		print('numsyscalc form:', nsys_form.is_valid())
		if nsys_form.is_valid():
			NumSysRes = TranslaterSS(request.POST).translateSS()
			initial_num = request.POST['calc_input']
			initial_ss = request.POST['other_ss'] if request.POST['ss'] == '-' else request.POST['ss']
			next_ss = request.POST['other_ss1'] if request.POST['ss1'] == '-' else request.POST['ss1']
			MathExp(initial_num=initial_num, initial_ss=initial_ss, next_ss=next_ss, next_num=NumSysRes).save()
			css = (('none', ''), ('none', ''), ('block', 'active'), ('none', ''))
		elif calc_form.is_valid():
			MathExp(initial_num=request.POST['mathExp'], next_num=request.POST['mathExpInput']).save()
			css = (('none', ''), ('block', 'active'), ('none', ''), ('none', ''))
		else:
			css = (('block', 'active'), ('none', ''), ('none', ''), ('none', ''))

		nmes = ('display', 'class')
		context = {
			'CalcForm': calc_form,
			'NumSysCalcForm': nsys_form,
			'ReportForm': ReportForm(),  # rep_form
			'resultNumSysCalcForm': NumSysRes,
			'intro_css': {nme:vl for nme, vl in zip(nmes, css[0])},
			'calc_css': {nme:vl for nme, vl in zip(nmes, css[1])},
			'NumSys_css': {nme:vl for nme, vl in zip(nmes, css[2])},
			'Rep_css': {nme:vl for nme, vl in zip(nmes, css[3])}
		}
	else:
		print("GET:", request.GET)
		context = {
			'CalcForm': CalcForm(),
			'NumSysCalcForm': NumSysCalcForm(),
			'ReportForm': ReportForm(),
			'resultNumSysCalcForm': '', 
			'intro_css': {'display': request.GET.get('display_intro', 'block'), 'class': request.GET.get('class_intro', 'active')},
			'calc_css': {'display': 'none', 'class': ''},
			'NumSys_css': {'display': 'none', 'class': ''},
			'Rep_css': {'display': request.GET.get('display_rep', 'none'), 'class': request.GET.get('class_rep', '')}
		}
	context['history'] = MathExp.objects.order_by('-id')[:10]
	return render(request, './index.html', context=context)


def thanks_page(request):
	if request.method == 'POST':
		SendTg(request.POST)
		name = request.POST['name'] if request.POST['name'] else 'Undefined'
		return render(request, './thanks.html', context={'name': name})
	elif request.GET.get('name') is not None:
		return render(request, './thanks.html', context={'name': request.GET['name']})
	else:
		return redirect('main_page', permanent=False)

# 'displayMiniPages': ['block', 'none', 'none', 'none', 'none', 'none']
# ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding', '_files', '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_post', '_read_started', '_set_content_type_params', '_set_post', '_stream', '_upload_handlers', 'accepted_types', 'accepts', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_signed_cookie', 'headers', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user']

def about_page(request):
	return render(request, './about.html')


def pageNotFound(request, exception):
	"""
	when user write invalid url
	"""
	return HttpResponseNotFound(f'<h1>Page Not found</h1><h1>404</h1><h1>{exception}</h1>')


def serverError(request):
	"""
	when will occur fatal server error,
	error in python code
	"""
	return HttpResponseServerError("<h1>Server died</h1><h2>500</h2><h3>Don't care about this. You need to know that web developer is too lazy to fix it</h3><h4>hehehe</h4>")

