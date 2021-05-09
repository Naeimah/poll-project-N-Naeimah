from django.db import models


# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
  )


class poll(models.Model):

  title = models.CharField(max_length=200, unique=True)
  question = models.CharField(max_length=200, unique=True)
  active_until = models.DateTimeField(auto_now_add=True)
  id = models.BigAutoField(primary_key=True)
  status = models.IntegerField(choices=STATUS,default=0)

class options (models.Model):
  title = models.CharField(max_length=200, unique=True)
  poll = models.ForeignKey("poll", on_delete=models.CASCADE)

  
class response(models.Model):
  name = models.CharField(max_length=200, unique=True)
  response_time = models.DatetimeField(auto_now_add= True)
  options = models.ForeingKey("options", default =None , on_delete = models.CASECADE)

