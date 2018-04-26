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

@method_decorator(csrf_exempt, name='dispatch')
class Install(View):

    _schema = {
        'name': {
            'type': 'string'
        }
    }

    def post(self, request):

        try:

            v = Validator(self._schema)
            body = request.body.decode('utf-8')
            body_document = json.loads(body)
            pprint(v.validate(body_document))

            return JsonResponse({"status":"d"})

        except Exception as e:
            return JsonResponse({
                "errors":[{
                    "message":"Access forbidden due to invalid or expired CSRF token!", "code":43
                }]
            }, status=500)

        else:
            pass
        finally:
            pass