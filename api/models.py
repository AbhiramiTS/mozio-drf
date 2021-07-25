from django.db import models
# from django.contrib.gis.db import models as poly_models

class Provider(models.Model):
    name = models.CharField(max_length = 100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=100, null=True)
    currency = models.CharField(max_length = 100, null=True)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, null=True, on_delete= models.SET_NULL)
    name = models.CharField(max_length = 100, blank=True, null=True)
    price = models.FloatField(default = 0.00)
    coordinates = models.TextField()

    def __str__(self):
        return self.name