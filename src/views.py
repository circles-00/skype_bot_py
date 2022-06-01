import os

from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

from src.services.skype_service import SkypeService
import environ

env = environ.Env()
environ.Env.read_env()

skype_service = SkypeService(os.environ.get('USERNAME'), os.environ.get('PASSWORD'))


@api_view(['GET', 'POST'])
def webhooks(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        return Response('GET')

    elif request.method == 'POST':
        json_data = json.loads(request.body)
        # print(json.dumps(json_data, indent=1))
        print(f"A new deploy has gone live: \n - Author {json_data['user_name']} \n - Message: {json_data['commits'][0]['message']}")
        skype_service.send_message(f"A new deploy has gone live: \n - Author {json_data['user_name']} \n - Message: {json_data['commits'][0]['message']} \n [This is an automated message, please wait for at least 10 mins for the deployment process to finish]")
        return Response('POST')
