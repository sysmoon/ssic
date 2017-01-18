from django.shortcuts import render
from .models import App
from django.utils import timezone

# Create your views here.

def post_list(request):
    apps = App.objects.filter(pubDate__lte=timezone.now()).order_by('pubDate')
    return render(request, "apprecog/app_list.html", {'apps': apps})