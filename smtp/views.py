from django.shortcuts import render, HttpResponse
from .tasks import *

def send_mail_to_u(request):
    smtp_func.delay()
