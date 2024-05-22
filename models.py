from django.db import models

# Create your models here.
# It doens't matter which database that we use. Django will create the code for it.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # This will create a timestamp
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
# At the end, you will need to make a migration (python3 manage.py makemigrations)
