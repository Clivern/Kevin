"""
Install API Endpoint
"""

from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from pprint import pprint
from cerberus import Validator
import json

#@method_decorator(csrf_exempt, name='dispatch')
class Install(View):

    def post(self, request):
        pprint(request.GET)
        pprint(request.POST["hi"])
        return JsonResponse({"status":"d"})