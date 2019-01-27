from django.shortcuts import render
from .models import Phrase
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.http import JsonResponse
from .models import Phrase, Intent
import boto3


@api_view()
def respond(request):
    # normalize the phrase
    phrase = request.GET.get('phrase').lower()

    try:
        # see if phrase exists in db and get its intent
        intent = Phrase.objects.get(name=phrase).intent
    except:
        client = boto3.client('lex-runtime')

        # send input to lex and get back the correct intent
        response = client.post_text(
            botName='robin',
            botAlias='robin',
            userId='testing',  # this should be unique for each client
            # sessionAttributes={'string': 'string'}, # optional
            # requestAttributes={'string': 'string'}, # optional
            inputText=phrase)

        intent = Intent.objects.get(name=response['message'])

        # add phrase to db and associate it with the intent
        Phrase.create(name=phrase, intent=intent)

    # trigger intent-specific method
    return JsonResponse({'response': intent.name})
