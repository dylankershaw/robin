from django.shortcuts import render
from .models import Phrase
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.http import JsonResponse
from .models import Phrase, Intent
from .intent_methods import IntentMethods
import boto3


@api_view()
def respond(request):
    # normalize the phrase
    phrase = request.GET.get('phrase').lower()

    try:
        # see if phrase exists in db and get its intent
        intent = Phrase.objects.get(name=phrase).intent
        slots = {}
    except:
        client = boto3.client('lex-runtime')

        # send input to lex and get back the correct intent
        lex_response = client.post_text(
            botName='robin',
            botAlias='robin',
            userId='testing',  # this should be unique for each client TODO: make this an env var
            # sessionAttributes={'string': 'string'}, # optional
            # requestAttributes={'string': 'string'}, # optional
            inputText=phrase)

        intent = Intent.objects.get(name=lex_response['intentName'])
        slots = lex_response['slots']

        # add phrase to db and associate it with the intent
        Phrase.create(name=phrase, intent=intent)

    # trigger intent-specific method
    method_response = getattr(IntentMethods, intent.name)(**slots)
    return JsonResponse({'response': method_response})
