"""
Routes For Kevin
"""

# Django
from django.contrib import admin
from django.urls import include, path

# local Django
from app.controllers.web.home import Home as Home_View
from app.controllers.web.install import Install as Install_View
from app.controllers.web.not_found import Not_Found as Not_Found_View
from app.controllers.web.error import Error as Error_View
from app.controllers.web.login import Login as Login_View
from app.controllers.web.register import Register as Register_View
from app.controllers.web.forgot_password import Forgot_Password as Forgot_Password_View
from app.controllers.web.reset_password import Reset_Password as Reset_Password_View
from app.controllers.web.admin.logout import Logout as Logout_View
from app.controllers.web.admin.dashboard import Dashboard as Dashboard_View
from app.controllers.web.admin.profile import Profile as Profile_View
from app.controllers.web.admin.namespaces import Namespaces as Namespaces_View
from app.controllers.web.admin.namespace import Namespace as Namespace_View
from app.controllers.web.admin.endpoint import Endpoint as Endpoint_View
from app.controllers.api.private.v1.install import Install as Install_V1_Endpoint_Private
from app.controllers.api.private.v1.login import Login as Login_V1_Endpoint_Private
from app.controllers.api.private.v1.register import Register as Register_V1_Endpoint_Private
from app.controllers.api.private.v1.forgot_password import Forgot_Password as Forgot_Password_V1_Endpoint_Private
from app.controllers.api.private.v1.reset_password import Reset_Password as Reset_Password_V1_Endpoint_Private


urlpatterns = [
    # Public Views
    path('', Home_View.as_view(), name='app.web.home'),
    path('install', Install_View.as_view(), name='app.web.install'),
    path('404', Not_Found_View.as_view(), name='app.web.not_found'),
    path('500', Error_View.as_view(), name='app.web.error'),
    path('login', Login_View.as_view(), name='app.web.login'),
    path('register', Register_View.as_view(), name='app.web.register'),
    path('forgot-password', Forgot_Password_View.as_view(), name='app.web.forgot_password'),
    path('reset-password/<token>', Reset_Password_View.as_view(), name='app.web.reset_password'),

    # Authenticated Users Views
    path('admin/', include([
        path('logout/<token>', Logout_View.as_view(), name='app.web.admin.logout'),
        path('dashboard', Dashboard_View.as_view(), name='app.web.admin.dashboard'),
        path('profile', Profile_View.as_view(), name='app.web.admin.profile'),
        path('namespaces', Namespaces_View.as_view(), name='app.web.admin.namespaces'),
        path('namespace/<slug:namespace>', Namespace_View.as_view(), name='app.web.admin.namespace'),
        path('namespace/<slug:namespace>/<slug:endpoint>', Endpoint_View.as_view(), name='app.web.admin.endpoint'),
    ])),

    # Private API V1 Endpoints
    path('api/private/v1/', include([
        path('install', Install_V1_Endpoint_Private.as_view(), name='app.api.private.v1.install.endpoint'),
        path('login', Login_V1_Endpoint_Private.as_view(), name='app.api.private.v1.login.endpoint'),
        path('register', Register_V1_Endpoint_Private.as_view(), name='app.api.private.v1.register.endpoint'),
        path('forgot-password', Forgot_Password_V1_Endpoint_Private.as_view(), name='app.api.private.v1.forgot_password.endpoint'),
        path('reset-password', Reset_Password_V1_Endpoint_Private.as_view(), name='app.api.private.v1.reset_password.endpoint'),
    ])),

    # Public API V1 Endpoints
    path('api/public/v1/', include([

    ]))
]