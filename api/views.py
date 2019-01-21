from django.shortcuts import render
from .models import Phrase
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.http import JsonResponse
from .models import Phrase, Intent


@api_view()
def respond(request):
    phrase = request.GET.get('phrase').lower()

    try:
        # see if phrase exists in db and get its intent
        intent = Phrase.objects.get(name=phrase).intent
    except:
        # send input to watson and get back the correct intent
        # add phrase to db and associate it with the intent

        # intent_name = # watson response

        # intent = Intent.objects.get(name=intent_name)
        # Phrase.objects.create(phrase, intent)

        intent = {'name': 'no intent found'}

    # trigger intent-specific method
    return JsonResponse({'response': intent.name})
