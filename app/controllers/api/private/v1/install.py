"""
Install API Endpoint
"""

from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from pprint import pprint
from app.modules.validation.form import Form

@method_decorator(csrf_exempt, name='dispatch')
class Install(View):

    def post(self, request):
        return JsonResponse({"status":"d"})