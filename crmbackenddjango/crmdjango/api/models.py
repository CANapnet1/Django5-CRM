from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.CharField(max_length=10, null=True)
    client_firstname = models.CharField(max_length=100, null=True)
    client_lasttname = models.CharField(max_length=100, null=True)
    client_date = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.client_lasttname

class ClientDetails(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.CharField(max_length=10, null=True)
    client_genre = models.CharField(max_length=50, null=True)
    client_rating = models.IntegerField(null=True)

    def __str__(self):
        return self.client_id