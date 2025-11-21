from django.db import models

# Create your models here.
class POLL(models.Model):
        subject=models.CharField("投票主題",max_length=64)
        desc=models.TextField("說明")
        created=models.DateField("建立日期")
       
        def __str__(self):
                return self.subject
class Option(models.Model):
        titel=models.CharField("選項文字",max_length=64)
        votes=models.IntegerField("票數",default=0)
        poll_id=models.DateField("投票主題編號")

        def __str__(self):
                return"{}-{}". format(self.poll_id,self.titel)
                return f"{self.poll_id}-{self.titel}"