"""
Logout Web Controller
"""

# Django
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect


class Logout(View):


    def get(self, request, token):
        pass