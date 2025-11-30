from django.urls import path
from .views import index, TestPageView, OurTeamView, About

app_name = 'landing'

urlpatterns = [
    path('', index, name='index'),
    path('test/', TestPageView.as_view(), name='test'),
    path('ourteam/', OurTeamView.as_view(), name='ourteam'),
    path('about/', About.as_view(), name='about')
]

