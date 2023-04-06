from django.contrib import admin
from django.urls import path
from walletApp import views # เอาไฟล์ viwes.py เข้ามาทำงานในนี้

urlpatterns = [
    path('', views.index),
    path('account', views.account)
]