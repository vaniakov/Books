# -*- coding: utf-8 -*-

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello, current_datetime, hours_ahead, display_meta, my_image, hello_pdf, hello_pdf1
import books.views as views
from books.views import PublisherListView, BooksListView,register, Test
from django.conf import settings
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^meta/$', display_meta),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', Test.as_view()),
    url(r'^contact/$', views.contact),
    url(r'^contact/thanks/$', views.thanks),
    url(r'^publisher/$', PublisherListView.as_view()),
    url(r'^books/$', BooksListView.as_view()),
    url(r'^image/$', my_image),
    url(r'^hello-pdf/$', hello_pdf),
    url(r'^hello-pdf1/$', hello_pdf1),
    url(r'^account/login/$', login),
    url(r'^account/loguot/$', logout),
    url(r'^registration/$', register),
    url(r'^banners/', include('banners.urls')),
]

from django.conf.urls.static import  static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)