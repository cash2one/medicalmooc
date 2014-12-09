"""
Views for returning XModule JS (used by requirejs)
"""
import os
import json
import datetime

from django.contrib.auth.decorators import login_required
from django_future.csrf import ensure_csrf_cookie
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from util.json_request import JsonResponse
from edxmako.shortcuts import render_to_response


from ..models import *
from ..image import *


@login_required
@ensure_csrf_cookie
def clientluobo(request):
    image_list = CustomImage.objects.filter(type=3).order_by('order_num', 'id')
    return render_to_response('syscustom/index_clientluobo.html', {'store_url':settings.STORE_URL, 'image_list':image_list})

def clientluobo_edit(request, id=None):
    if request.method == 'POST':
        image = request.POST.get('image', '')
        url = request.POST.get('url', '')
        order_num = request.POST.get('order_num')
        try:
            order_num = int(order_num)
        except:
            order_num = 1
        
        if id:
            obj = CustomImage.objects.get(id=id)
            obj.updated_time = datetime.datetime.now()
        else:
            obj = CustomImage()
        obj.img = image
        obj.url = url
        obj.order_num = order_num
        obj.type = 3
        obj.save()
        
        return redirect(reverse('clientluobo'))
    else:
        obj = None
        if id:
            obj = CustomImage.objects.get(id=id)
        return render_to_response('syscustom/clientluobo_edit.html', {'obj':obj})

    
