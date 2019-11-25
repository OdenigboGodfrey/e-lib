from django.db import models

# Create your models here.
class registration(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    first_name = models.CharField(max_length=40, blank=False, null=False )
    last_name = models.CharField(max_length=40, blank=False, null=False)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    dob = models.CharField(max_length=60, blank=False, null=False)
    gender = models.CharField(max_length=1,blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    signed_up_on = models.DateTimeField(auto_now=True, blank=False, null=False)
    user_recorded = models.IntegerField(blank=False, null=False, default=-1)

    def __str__(self):
        return self.email

