# Create your views here.
from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def main(request):
    logger.info('Main page accessed')
    return HttpResponse("It's my first Django site")


def about(request):
    logger.info('About page accessed')
    return HttpResponse("Here must be some information about myself, but my fantasy failed me")
