from django.db import models


# Create your models here.
# make migrations- see the changes in the modals
# migrate-apply all the changes in the models such as create the table
# after creating go to admin.py register the modals
# step 3 go to setting in installed app register the app name
class booking(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    subject = models.TextField(default='')
    message = models.TextField()
    date = models.DateTimeField

    def __str__(self):
     return self.name