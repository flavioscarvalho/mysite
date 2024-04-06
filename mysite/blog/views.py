from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse

class PostView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Resposta da view PostView para GET')
