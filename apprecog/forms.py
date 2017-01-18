__author__ = 'sysmoon'

from django import forms
from .models import App

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ('listIdx', 'category', 'appName', 'sppServerity', 'corpName', 'summary', 'readCnt', 'regId', 'regDate', 'updId', 'updDate', 'delFlag', 'pubDate')