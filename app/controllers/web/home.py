"""
Home Web Controller
"""

from django.http import HttpResponse
from django.template import loader


class Home():

	def index(self):
	    template = loader.get_template('templates/home.html')
	    response_body = template.render({'foo': 'bar'})
	    return HttpResponse(response_body)