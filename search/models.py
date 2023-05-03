from django.db import models


class SearchResult(models.Model):
    link = models.URLField(null=True,blank=True)
    title = models.CharField(null=True,blank=True,max_length=100)
    position = models.IntegerField(default=0)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.link})"

class Blocked(models.Model):
    link = models.URLField(null=True,blank=True)
    title = models.CharField(null=True,blank=True,max_length=100)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.link})"

class Searches(models.Model):
    query = models.CharField(null=True, blank=True, max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.query} ({self.timestamp})"
