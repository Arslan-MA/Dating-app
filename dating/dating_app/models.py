from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    profession = models.CharField(max_length=50)
    hobby = models.CharField(max_length=80)
    about_me = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.surname}"

    def get_absolute_url(self):
        return f"/profile/{self.id}"
