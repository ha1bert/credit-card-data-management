"""gyq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('/', views.index),
    path('axis_login/', views.axis_login),
    path('main_2/', views.main_2),
    path('main_2/persional/', views.persional),
    path('main_2/persional/axis_persional/', views.axis_persional),
    path('main_2/xgmm/', views.xgmm),
    path('main_2/xgmm/axis_xgmm/', views.axis_xgmm),
    path('main_2/data_manage/', views.data_manage),
    path('main_2/data_manage/data_json/', views.data_json),
    path('main_2/data_manage/axis_data/', views.axis_data),
    path('main_2/data_manage/data_add/', views.data_add),
    path('main_2/data_manage/data_add/axis_data/', views.axis_data),
    path('main_2/data_manage/data_updata/', views.data_updata),
    path('main_2/data_manage/data_updata/axis_data/', views.axis_data),
    
    path('main_1/', views.main_1),
    path('main_1/persional/', views.persional),
    path('main_1/persional/axis_persional/', views.axis_persional),
    path('main_1/xgmm/', views.xgmm),
    path('main_1/xgmm/axis_xgmm/', views.axis_xgmm),

    path('main_1/data_manage/', views.data_manage),
    path('main_1/data_manage/data_json/', views.data_json),
    path('main_1/data_manage/axis_data/', views.axis_data),
    path('main_1/data_manage/data_add/', views.data_add),
    path('main_1/data_manage/data_add/axis_data/', views.axis_data),
    path('main_1/data_manage/data_updata/', views.data_updata),
    path('main_1/data_manage/data_updata/axis_data/', views.axis_data),

    path('main_1/login_manage/', views.login_manage),
    path('main_1/login_manage/login_json/', views.login_json),
    path('main_1/login_manage/axis_manage_login/', views.axis_manage_login),
    path('main_1/login_manage/login_add/', views.login_add),
    path('main_1/login_manage/login_add/axis_manage_login/', views.axis_manage_login),
    path('main_1/login_manage/login_updata/', views.login_updata),
    path('main_1/login_manage/login_updata/axis_manage_login/', views.axis_manage_login),
    
    
]
