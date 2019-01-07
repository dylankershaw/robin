from django.shortcuts import render
from .models import Phrase
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.http import JsonResponse


@api_view()
def respond(request):
    response = request.GET.get('query')
    # TODO:
    # find or create phrase
    # trigger intent-specific method
    # return appropriate response from that method
    return JsonResponse({'query': response})
