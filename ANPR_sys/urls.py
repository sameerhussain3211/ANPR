"""ANPR_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from plateDetection.views import plateView, addUsers, index, addUserScreen, getRecords, individualDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index-page'), #BASE PAGE
    path('plateView/', plateView), 
    path('addUserScreen/', addUserScreen, name='add_user_screen'),
    path('addUser/', addUsers, name='add-users'),
    path('records/', getRecords, name="records"),
    path('individual/', individualDetails, name="individual"),
]
