from django.db import models

# Create your models here to store in the DB
# Once you create a new model, you should migrate do the db
# by running 
# python manage.py makemigrations
# python manage.py migrate
class Message(models.Model):
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.message

