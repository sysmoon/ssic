from django.db import models
from django.utils import timezone

# Create your models here.

class App(models.Model):
    author = models.ForeignKey('auth.User')
    listIdx = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)
    appName = models.CharField(max_length=30, null=False)
    sppServerity = models.CharField(max_length=10)
    corpName = models.CharField(max_length=50, null=False)
    summary = models.CharField(max_length=255)
    readCnt = models.PositiveIntegerField()
    regId = models.CharField(max_length=50, null=False)
    regDate = models.DateField(null=False)
    updId = models.CharField(max_length=50, null=False)
    updDate = models.DateField(null=False)
    delFlag = models.CharField(max_length=1)
    pubDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.pubDate = timezone.now()
        self.save()

    def __str__(self):
        return self.appName