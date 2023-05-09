from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponseServerError

# Create your views here.
def about_page(request):
    if request.method == 'POST':
        name = request.POST['name'] if request.POST['name'] else 'Undefined'
        email = request.POST['email']
        message = f'Name: {name}\nEmail: {email}\nMessage: '
        message += request.POST['message']
        try:
            send_mail(
            f'CV Form from {name} has received',
            message,
            'settings.EMAIL_HOST_USER',
            [eval('settings.EMAIL_HOST_USER')],
            fail_silently=False
            )
        except BadHeaderError:
            return HttpResponseServerError('BadHeaderError has been occured')
        except Exception as e:
            print('Exception', e, dir(e))
            return HttpResponseServerError()
        return HttpResponseRedirect(f'../thanks/?name={name}')
    return render(request, './about.html')


def youtube_page(request):
    return render(request, './youtube.html')