# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from books.models import Book, Publisher
from forms import ContactForm

# Create your views here.
def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    error = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error.append('Введіть пошуковий запит!')
        elif len(q) > 20:
            error.append('Запит не повинен перевищувати 20 символів!')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',{'books':books, 'query':q})

    return render_to_response('search_form.html',{'error':error})

# def contact(request):
#     errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject', ''):
#             errors.append('Enter subject')
#         if not request.POST.get('message', ''):
#             errors.append('Enter message')
#         if not request.POST.get('e-mail') and '@' not in request.POST['e-mail']:
#             errors.append('Enter correct e-mail')
#         if not errors:
#             send_mail(
#                 request.POST['subject'],
#                 request.POST['message'],
#                 request.POST.get('e-mail', 'noreply@example.com'),
#                 ['siteowner@example.com'],
#             )
#         return HttpResponseRedirect('/contact/')
#     return render_to_response('contact_form.html',{'error':errors})

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('e-mail','noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject':"I like your site"})
    return render_to_response('contact_form.html', {'form': form})

def thanks(request):
    return render_to_response('thamks.html', {'a':request.META['HTTP_REFERER']})

from django.views.generic.list import ListView


class PublisherListView(ListView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super(PublisherListView, self).get_context_data(**kwargs)
        return context

class BooksListView(ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BooksListView, self).get_context_data(**kwargs)
        return context


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf


def register(request):
    c = {}
    c.update(csrf(request))
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/books/")
    else:
        form = UserCreationForm()
        c['form'] = form
    return render_to_response("registration/register.html", c)
