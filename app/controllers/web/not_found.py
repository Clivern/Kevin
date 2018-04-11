"""
NotFound Web Controller
"""

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

class NotFound(View):

	template_name = 'templates/404.html'

	def get(self, request):
	    return render(request, self.template_name, {'page_title': '404'})