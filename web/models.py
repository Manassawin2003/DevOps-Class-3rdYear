from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    story = models.TextField()
    projectdevelop = models.TextField()
    tooldevelop = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Addnewfield(models.Model):
    profile = models.ForeignKey(Profile, related_name='fields', on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.TextField()

    def __str__(self):
        return self.key

class Visitor(models.Model):
    url = models.CharField(max_length=255)  # URL of the page being visited
    visit_count = models.IntegerField(default=0)  # Number of visits
    last_visited = models.DateTimeField(auto_now=True)  # Automatically updates on each visit

    def __str__(self):
        return f"{self.url} - {self.visit_count} visits"