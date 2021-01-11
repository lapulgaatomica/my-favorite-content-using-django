from django.db import models

class DailyMailColumn(models.Model):
    link = models.CharField(max_length=2083, unique=True)
    title = models.CharField(max_length=2083)
    columnist = models.CharField(max_length=2083)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
