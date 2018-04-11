"""
Forgot Password Web Controller
"""

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

class ForgotPassword(View):

	template_name = 'templates/forgot_password.html'

	def get(self, request):
	    return render(request, self.template_name, {'page_title': 'Forgot Password'})