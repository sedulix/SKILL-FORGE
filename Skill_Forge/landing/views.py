from django.shortcuts import render
from django.views import View


def index(request):
    return render(request, 'landing/index.html')


class TestPageView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'landing/test.html', context)


class OurTeamView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'landing/ourteam.html', context)


class About(View):
    def get(self, request):
        context = {

        }
        return render(request, 'landing/about.html', context)


