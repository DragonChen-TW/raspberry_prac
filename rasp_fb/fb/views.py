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
    def get(self, request):
        if request.GET.get('hub.mode') == 'subscribe' and request.GET.get('hub.challenge'):
            if request.GET.get('hub.verify_token') == 'Small_Dragon_TW':
                return HttpResponse(request.GET.get('hub.challenge'), status=200)
            else:
                return HttpResponse('Verify Fail', status=403)
        else:
            return HttpResponse('Hello, world', status=200)

    def post(self, request):
        data = json.loads(request.body)
        if data['object'] == 'entry':
            print(data['entry'])
            for msg_event in entry['messaging']:
                sender_id = msg_event['sender']['id']
                # msg_event
                if msg_event['message']:
                    message_text == 'turn on led'
