from django.db import models


# Create your models here.
class RouteOutput(models.Model):
    route = models.Field()
    map_url = models.Field()