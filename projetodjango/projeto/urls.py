from django.urls import path
from aplicativo import views

urlpatterns = [
    path('',views.home, name='home')
]
