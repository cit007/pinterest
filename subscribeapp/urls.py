from django.urls import path
from django.views.generic import TemplateView

from subscribeapp.views import SubscribeView

app_name = "subscribeapp"

urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
]
