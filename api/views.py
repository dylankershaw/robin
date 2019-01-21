from django.shortcuts import render
from .models import Phrase
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.http import JsonResponse
from .models import Phrase


@api_view()
def respond(request):
    phrase = request.GET.get('phrase')
    # TODO:
    # find or create phrase
    try:
      response = Phrase.objects.get(name=phrase).name
      print(response)
    except:
      response = 'no response found'
    # trigger intent-specific method
    # return appropriate response from that method
    return JsonResponse({'phrase': response})
