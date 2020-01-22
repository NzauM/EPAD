from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static

urlpatterns=[
    path('dashboard/',views.dashboard,name='user-dashboard'),
    path('users/',views.registered_users,name='system_users'),
    path('user/activate/<int:id>',views.user_activate,name='activate_user'),
    path('user/deactivate/<int:id>',views.user_deactivate,name='deactivate_user'),
]