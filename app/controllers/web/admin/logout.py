"""
Logout Web Controller
"""

# Django
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# local Django
from app.modules.core.context import Context


class Logout(View):

    _context = Context()


    def get(self, request, token):
        pass