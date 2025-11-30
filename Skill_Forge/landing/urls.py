from django.urls import path
from . views import index, TestPageView

app_name = 'landing'

urlpatterns = [
    path('', index, name='index'),
    path('test/', TestPageView.as_view(), name='test'),
]


