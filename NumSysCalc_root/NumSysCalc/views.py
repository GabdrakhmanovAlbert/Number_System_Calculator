
# from pprint import PrettyPrinter, pprint
from calc.apps import TranslaterSS
from calc.forms import CalcForm, NumSysCalcForm
from calc.models import NumSysExp, MathExp
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import redirect, render
from django.template import loader
from report.forms import ReportForm
from report.sendMessage import SendTg
# import asyncio
from asgiref.sync import sync_to_async
# views


def main_page(request):
	return render(request, './index.html', {'nav_bar': ['active', '', '', '', '', '']})


def thanks_page(request):
	if request.method == 'POST':
		sync_to_async(SendTg(request.POST))
		name = request.POST['name'] if request.POST['name'] else 'Undefined'
		return render(request, './thanks.html', context={'name': name})
	elif request.GET.get('name') is not None:
		return render(request, './thanks.html', context={'name': request.GET['name']})
	else:
		return redirect('main_page', permanent=False)

# 'displayMiniPages': ['block', 'none', 'none', 'none', 'none', 'none']
# ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding', '_files', '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_post', '_read_started', '_set_content_type_params', '_set_post', '_stream', '_upload_handlers', 'accepted_types', 'accepts', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_signed_cookie', 'headers', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user']


def calc_page(request):
	context = {
		'nav_bar': ['', 'active', '', '', '', ''],
	}
	if request.POST:
		calc_form = CalcForm(request.POST)
		print('calc form:', calc_form.is_valid())
		print(request.POST)
		if calc_form.is_valid():
			print('save')
			MathExp(express=request.POST['mathExp'], res=request.POST['mathExpInput']).save()
		context['CalcForm'] = calc_form
	else:
		context['CalcForm'] = CalcForm()
	return render(request, './calc.html', context=context)



# def main_page(request):
# 	global NumSysRes
# 	if request.POST:
# 		print("POST:", request.POST)
# 		nsys_form = NumSysCalcForm(request.POST)
# 		if nsys_form.is_valid():
# 			NumSysRes = TranslaterSS(request.POST).translateSS()
# 			initial_num = request.POST['calc_input']
# 			initial_ss = request.POST['other_ss'] if request.POST['ss'] == '-' else request.POST['ss']
# 			next_ss = request.POST['other_ss1'] if request.POST['ss1'] == '-' else request.POST['ss1']
# 			NumSysExp(initial_num=initial_num, initial_ss=initial_ss, next_ss=next_ss, next_num=NumSysRes).save()
# 			css = (('none', ''), ('none', ''), ('block', 'active'), ('none', ''))
# 		else:
# 			css = (('block', 'active'), ('none', ''), ('none', ''), ('none', ''))

# 		nmes = ('display', 'class')
# 		context = {
# 			'NumSysCalcForm': nsys_form,
# 			'ReportForm': ReportForm(),  # rep_form
# 			'resultNumSysCalcForm': NumSysRes,
# 			'intro_css': {nme:vl for nme, vl in zip(nmes, css[0])},
# 			'calc_css': {nme:vl for nme, vl in zip(nmes, css[1])},
# 			'NumSys_css': {nme:vl for nme, vl in zip(nmes, css[2])},
# 			'Rep_css': {nme:vl for nme, vl in zip(nmes, css[3])}
# 		}
# 	else:
# 		print("GET:", request.GET)
# 		context = {
# 			'CalcForm': CalcForm(),
# 			'NumSysCalcForm': NumSysCalcForm(),
# 			'ReportForm': ReportForm(),
# 			'resultNumSysCalcForm': '', 
# 			'intro_css': {'display': request.GET.get('display_intro', 'block'), 'class': request.GET.get('class_intro', 'active')},
# 			'calc_css': {'display': 'none', 'class': ''},
# 			'NumSys_css': {'display': 'none', 'class': ''},
# 			'Rep_css': {'display': request.GET.get('display_rep', 'none'), 'class': request.GET.get('class_rep', '')}
# 		}
# 	context['history'] = NumSysExp.objects.order_by('-id')[:10]
# 	return render(request, './index.html', context=context)


NumSysRes = ''

def numsyscalc_page(request):
	global NumSysRes
	context = {
		'nav_bar': ['', '', 'active', '', '', '']
	}
	if request.POST:
		calc_form = NumSysCalcForm(request.POST)
		print('nsyscalc_form:', calc_form.is_valid())
		print(request.POST)
		if calc_form.is_valid():
			NumSysRes = TranslaterSS(request.POST).translateSS()
			initial_num = request.POST['calc_input']
			initial_ss = request.POST['other_ss'] if request.POST['ss'] == '-' else request.POST['ss']
			next_ss = request.POST['other_ss1'] if request.POST['ss1'] == '-' else request.POST['ss1']
			NumSysExp(initial_num=initial_num, initial_ss=initial_ss, next_ss=next_ss, next_num=NumSysRes).save()
			context['NumSysCalcForm'] = calc_form
		else:
			print('invalid NumSysForm')
			context['NumSysCalcForm'] = NumSysCalcForm()
		context['resultNumSysCalcForm'] = NumSysRes
	else:
		context['NumSysCalcForm'] = NumSysCalcForm()
		context['resultNumSysCalcForm'] = ''
	return render(request, './NumSysCalc.html', context=context)


def theory_page(request):
	return render(request, './theory.html', context={'nav_bar': ['', '', '', 'active', '', '']})


def data_page(request):
	nsys_data = NumSysExp.objects.order_by('-id')[:10]
	calc_data = MathExp.objects.order_by('-id')[:10]
	ndata = sorted(list(nsys_data) + list(calc_data), key=lambda x: x.dt, reverse=True)[:10]
	return render(request, './history.html', context={'nav_bar': ['', '', '', '', 'active', ''], 'history': ndata})


def report_page(request):
	context = {
		'nav_bar': ['', '', '', '', '', 'active'],
		'ReportForm': ReportForm()
	}
	return render(request, './report.html', context=context)


def pageNotFound(request, exception):
	"""
	when user write invalid url
	"""
	# pprint(dir(request))
	# tloader = loader.get_template('./404.html')
	# resp = HttpResponseNotFound()
	# return HttpResponseNotFound(tloader.render({'exception': exception}, request), content_type='application/xhtml+xml')	
	# resp.status_code = 404

	return render(request, './404.html', context={'exception': exception},  status=404)


def serverError(request):
	"""
	when will occur fatal server error,
	error in python code
	"""
	return HttpResponseServerError("<h1>Server died</h1><h2>500</h2><h3>Don't care about this. You need to know that web developer is too lazy to fix it</h3><h4>hehehe</h4>")

