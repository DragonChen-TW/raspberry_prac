from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

import json, requests

# Create your views here.
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
        # fans 2119773578253322
        # personal 2449993941684764
        # personal 844603888893940

        data = json.loads(str(request.body, 'utf-8'))
        print(json.dumps(data))
        for entry in data['entry']:
            if 'messaging' in entry:
                for msg in entry['messaging']:
                    sender = msg['sender']['id']
                    msg = msg['message']['text']
                    print(sender, msg)
                    self.reply(sender, msg)
        return HttpResponse('okay', status=200)

    def reply(self, sender, send_msg):
        token = 'EAACEdEose0cBACyr14Hg0erhNrYZCGqPA2gDPpruAeGZA5wfhhMuYIa01xSJLPf29FC5FckLTj1nnNuHsVPDhziA1tvZAb9giGuIymJoZBDXDOUgqUjoZCaG7ruH2I54KW0kZCExfZBBRc7XD8FhJ4wisWISbSf7OboOxzLZB2jEuIExgMPVF80qbkSTcoMtr5J9KMFhGSH6xwZDZD'
        data = {
            'recipient': {'id': sender},
            'message': {'text': 'You just msg me "{}"\nHello there~'.format(send_msg)}
        }
        res = requests.post('https://graph.facebook.com/v3.0/me/messages?access_token={}'.format(token), json=data)
        print(res.content)
