"""NumSysCalc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

from . import views

urlpatterns = [
	path("admin/", admin.site.urls),
	path("", views.main_page, name='main_page'),
	path("thanks/", views.thanks_page, name='thanks_page'),
    path("about/", include('report.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})]


handler404 = views.pageNotFound
handler500 = views.serverError

# if settings.DEBUG is False:   #if DEBUG is True it will be served automatically
#     urlpatterns += patterns('',
#             url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#     )

# handlers woks only settings.DEBUG = False