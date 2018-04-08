from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from . import models

templates =__name__.split(".")[-2] + '/'

# Create your views here.

class Index(TemplateView):
    template_name = templates + 'index.html'