
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from myapi.core import views
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls, name='Admin Page'),
    path('hello/', views.HelloView.as_view(), name='Welcome Page'),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('checkserver/', index, name='index'),
    path('auth/', include('myapi.core.urls')),
]
