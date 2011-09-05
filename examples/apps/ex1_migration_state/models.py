from django.db import models


class HelloModel(models.Model):
	hello = models.CharField(max_length=5, default="Hello")
