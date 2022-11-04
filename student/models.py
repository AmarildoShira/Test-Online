from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=64, null=True, blank=True)
    last_name=models.CharField(max_length=64, null=True, blank=True)
    username=models.CharField(max_length=64, null=True, blank=True)
    password=models.CharField(max_length=64, null=True, blank=True)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name