"""
Forbidden Access Views
"""

from django.http import JsonResponse

def csrf_failure(request, reason=""):
	return JsonResponse({
			"errors":[{
				"message":"Access forbidden due to invalid or expired CSRF token!", "code":43
			}]
		}, status=403)