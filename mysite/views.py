# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date':now}))
    # return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        hours_offset = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours = hours_offset)
    return render_to_response("hours_ahead.html", locals())

def display_meta(request):
    values = request.META.items()
    values.sort()
    dt = dict(d=values, path=request.path)
    return render_to_response('meta.html', dt)

def my_image(request):
    img_data = open('mysite\img.jpg', 'rb').read()
    return HttpResponse(img_data, content_type ='image/jpg')

from reportlab.pdfgen import canvas

def hello_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
    p = canvas.Canvas(response)
    p.drawString(100, 100, "Hello World!")
    p.showPage()
    p.save()
    return response

from cStringIO import StringIO
from random import randint, choice
def hello_pdf1(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
    temp = StringIO()
    p = canvas.Canvas(temp)
    for i in range(0, 10000):
        p.drawString(randint(0, 1000), randint(0,1000), choice('.'))
    p.showPage()
    p.save()
    response.write(temp.getvalue())
    return response

