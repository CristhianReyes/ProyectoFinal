from django.shortcuts import render
from django.http import HttpResponse

def primer_vista(request):
    return HttpResponse("Primera Vista")
