from django.db import models
import datetime


class Files(models.Model):
    name = models.CharField("Название", max_length=100)
    discription = models.TextField("Описание", max_length=1000)
    file = models.FileField("Видео", upload_to='videos/%Y/%m/%d')
    date = models.DateField(("Date"), default=datetime.date.today)
