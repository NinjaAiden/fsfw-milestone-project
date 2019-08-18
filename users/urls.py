from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('register', TemplateView.as_view(template_name='register.html'), name='register')
]