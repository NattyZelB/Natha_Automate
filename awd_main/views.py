
from django.http import HttpResponse
from django.shortcuts import render
from dataentry.tasks import celery_test_task

def home(request):
    return render(request, 'home.html')

def celery_test(request):
    # I want toexecute a time comsuming task hier.
    celery_test_task.delay()
    return HttpResponse('<h3>Function executed successfully. </h3>')