from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json

# Create your views here.
# def index(request):
#     if request.method == 'GET':
#         if request.GET.get('hub.mode') == 'subscribe' and request.GET.get('hub.challenge'):
#             if request.GET.get('hub.verify_token') == 'Small_Dragon_TW':
#                 return HttpResponse(request.GET.get('hub.challenge'), status=200)
#             else:
#                 return HttpResponse('Verify Fail', status=403)
#         else:
#             return HttpResponse('Hello, world', status=200)
#     else:
#         pass

class index(View):
    def get(request):
        if request.GET.get('hub.mode') == 'subscribe' and request.GET.get('hub.challenge'):
            if request.GET.get('hub.verify_token') == 'Small_Dragon_TW':
                return HttpResponse(request.GET.get('hub.challenge'), status=200)
            else:
                return HttpResponse('Verify Fail', status=403)
        else:
            return HttpResponse('Hello, world', status=200)
    def post(request):
        with open('out.js', w) as js:
            js.write(request.body)
