"""
Install API Endpoint
"""

# Django
from django.views import View
from django.urls import reverse
from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# local Django
from app.modules.validation.form import Form
from app.modules.util.helpers import Helpers
from app.modules.core.profile import Profile as Profile_Module
from app.modules.core.request import Request
from app.modules.core.response import Response


class Profile(View):

    _request = Request()
    _response = Response()
    _helpers = Helpers()
    _form = Form()
    _settings = None
    _logger = None
    _user_id = None
    _profile_module = Profile_Module()


    def __init__(self):
        self._logger = self._helpers.get_logger(__name__)


    def post(self, request):

        self._user_id = request.user.id

        self._request.set_request(request)
        request_data = self._request.get_request_data("post", {
            "action" : ""
        })

        self._form.add_inputs({
            'action': {
                'value': request_data["action"],
                'validate': {
                    'any_of':{
                        'param': [["_update_profile", "_update_password", "_update_access_token", "_update_refresh_token"]],
                        'error': _("Error! Invalid Request.")
                    }
                }
            }
        })

        self._form.process()

        if not self._form.is_passed():
            return JsonResponse(self._response.send_private_failure(self._form.get_errors(with_type=True)))

        if self._form.get_input_value("action") == "_update_profile":
            return self._update_profile(request)
        elif self._form.get_input_value("action") == "_update_password":
            return self._update_password(request)
        elif self._form.get_input_value("action") == "_update_access_token":
            return self._update_access_token(request)
        elif self._form.get_input_value("action") == "_update_refresh_token":
            return self._update_refresh_token(request)


    def _update_profile(self, request):

        self._request.set_request(request)
        request_data = self._request.get_request_data("post", {
            "first_name" : "",
            "last_name" : "",
            "username" : "",
            "email" : "",
            "job_title" : "",
            "company" : "",
            "address" : "",
            "github_url" : "",
            "twitter_url" : "",
            "facebook_url" : ""
        })

        self._form.add_inputs({
            'first_name': {
                'value': request_data["first_name"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {
                    'names': {
                        'error': _('Error! First name contains invalid characters.')
                    },
                    'length_between':{
                        'param': [0, 20],
                        'error': _('Error! First name must be 1 to 20 characters long.')
                    }
                }
            },
            'last_name': {
                'value': request_data["last_name"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {
                    'names': {
                        'error': _('Error! Last name contains invalid characters.')
                    },
                    'length_between':{
                        'param': [0, 20],
                        'error': _('Error! Last name must be 1 to 20 characters long.')
                    }
                }
            },
            'username': {
                'value': request_data["username"],
                'sanitize': {
                    'escape': {},
                    'strip': {}
                },
                'validate': {
                    'alpha_numeric': {
                        'error': _('Error! Username must be alpha numeric.')
                    },
                    'length_between':{
                        'param': [4, 10],
                        'error': _('Error! Username must be 5 to 10 characters long.')
                    }
                }
            },
            'email': {
                'value': request_data["email"],
                'sanitize': {
                    'escape': {},
                    'strip': {}
                },
                'validate': {
                    'email': {
                        'error': _('Error! Admin email is invalid.')
                    }
                }
            },
            'job_title': {
                'value': request_data["job_title"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {
                    'length_between':{
                        'param': [0, 80],
                        'error': _('Error! Job title is very long.')
                    },
                    'optional': {}
                }
            },
            'company': {
                'value': request_data["company"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {
                    'length_between':{
                        'param': [0, 80],
                        'error': _('Error! Company is very long.')
                    },
                    'optional': {}
                }
            },
            'address': {
                'value': request_data["address"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {
                    'length_between':{
                        'param': [0, 80],
                        'error': _('Error! Address is very long.')
                    },
                    'optional': {}
                }
            },
            'github_url': {
                'value': request_data["github_url"],
                'sanitize': {
                    'escape': {},
                    'strip': {}
                },
                'validate': {
                    'url': {
                        'error': _('Error! Github url is invalid.')
                    },
                    'length_between':{
                        'param': [0, 80],
                        'error': _('Error! Github url is very long.')
                    },
                    'optional': {}
                }
            },
            'twitter_url': {
                'value': request_data["twitter_url"],
                'sanitize': {
                    'escape': {},
                    'strip': {}
                },
                'validate': {
                    'url': {
                        'error': _('Error! Twitter url is invalid.')
                    },
                    'length_between':{
                        'param': [0, 80],
                        'error': _('Error! Twitter url is very long.')
                    },
                    'optional': {}
                }
            },
            'facebook_url': {
                'value': request_data["facebook_url"],
                'sanitize': {
                    'escape': {},
                    'strip': {}
                },
                'validate': {
                    'url': {
                        'error': _('Error! Facebook url is invalid.')
                    },
                    'length_between':{
                        'param': [0, 80],
                        'error': _('Error! Facebook url is very long.')
                    },
                    'optional': {}
                }
            }
        })

        self._form.process()

        if not self._form.is_passed():
            return JsonResponse(self._response.send_private_failure(self._form.get_errors(with_type=True)))

        if self._profile_module.username_used_elsewhere(self._user_id, self._form.get_input_value("username")):
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Username is already used.")
            }]))


        if self._profile_module.email_used_elsewhere(self._user_id, self._form.get_input_value("email")):
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Email is already used.")
            }]))

        result = self._profile_module.update_profile(self._user_id, {
            "first_name": self._form.get_input_value("first_name"),
            "last_name": self._form.get_input_value("last_name"),
            "username": self._form.get_input_value("username"),
            "email": self._form.get_input_value("email"),
            "job_title": self._form.get_input_value("job_title"),
            "company": self._form.get_input_value("company"),
            "address": self._form.get_input_value("address"),
            "github_url": self._form.get_input_value("github_url"),
            "twitter_url": self._form.get_input_value("twitter_url"),
            "facebook_url": self._form.get_input_value("facebook_url")
        })

        if result:
            return JsonResponse(self._response.send_private_success([{
                "type": "success",
                "message": _("Profile updated successfully.")
            }]))

        else:
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while updating your profile.")
            }]))


    def _update_password(self, request):

        self._request.set_request(request)
        request_data = self._request.get_request_data("post", {
            "old_password" : "",
            "new_password" : ""
        })

        self._form.add_inputs({
            'old_password': {
                'value': request_data["old_password"],
                'validate': {
                    'password': {
                        'error': _("Error! Old password is invalid.")
                    },
                    'length_between':{
                        'param': [7, 20],
                        'error': _("Error! Old password is invalid.")
                    }
                }
            },
            'new_password': {
                'value': request_data["new_password"],
                'validate': {
                    'password': {
                        'error': _('Error! New Password must contain at least uppercase letter, lowercase letter, numbers and special character.')
                    },
                    'length_between':{
                        'param': [7, 20],
                        'error': _('Error! New Password length must be from 8 to 20 characters.')
                    }
                }
            }
        })

        self._form.process()

        if not self._form.is_passed():
            return JsonResponse(self._response.send_private_failure(self._form.get_errors(with_type=True)))

        if not self._profile_module.validate_password(self._user_id, self._form.get_input_value("old_password")):
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Old password is invalid.")
            }]))

        result = self._profile_module.change_password(self._user_id, self._form.get_input_value("new_password"))

        if result:
            self._profile_module.restore_session(self._user_id, request)
            return JsonResponse(self._response.send_private_success([{
                "type": "success",
                "message": _("Password updated successfully.")
            }]))

        else:
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while updating your password.")
            }]))


    def _update_access_token(self, request):

        self._request.set_request(request)
        request_data = self._request.get_request_data("post", {
            "token" : "",
        })

        self._form.add_inputs({
            'token': {
                'value': request_data["token"],
                'validate': {
                    'token':{
                        'error': _("Error! The provided token invalid, Please refresh the page.")
                    }
                }
            }
        })

        self._form.process()

        if not self._form.is_passed() and request_data["token"] != "":
            return JsonResponse(self._response.send_private_failure(self._form.get_errors(with_type=True)))


        result = self._profile_module.update_access_token(self._user_id)

        if result != False:
            return JsonResponse(self._response.send_private_success([{
                "type": "success",
                "message": _("Access token updated successfully.")
            }], {"token": result}))
        else:
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while updating access token.")
            }]))


    def _update_refresh_token(self, request):

        self._request.set_request(request)
        request_data = self._request.get_request_data("post", {
            "token" : "",
        })

        self._form.add_inputs({
            'token': {
                'value': request_data["token"],
                'validate': {
                    'token':{
                        'error': _("Error! The provided token invalid, Please refresh the page.")
                    }
                }
            }
        })

        self._form.process()

        if not self._form.is_passed() and request_data["token"] != "":
            return JsonResponse(self._response.send_private_failure(self._form.get_errors(with_type=True)))


        result = self._profile_module.update_refresh_token(self._user_id)

        if result != False:
            return JsonResponse(self._response.send_private_success([{
                "type": "success",
                "message": _("Refresh token updated successfully.")
            }], {"token": result}))
        else:
            return JsonResponse(self._response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while updating refresh token.")
            }]))