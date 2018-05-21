from django.shortcuts import render
from django.http import HttpResponse

from .models import FileData
from connect.dropbox import make_connection

def index(request):
    return HttpResponse("Index")