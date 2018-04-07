""" Kevin
Tool to Inspect HTTP Requests & Build Custom Endpoints.

@author: Clivern U{hello@clivern.com}
"""
from django.http import HttpResponse


class Home():

	def index(self):
		return HttpResponse("Hello World")