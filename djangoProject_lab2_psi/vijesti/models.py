import datetime

from django.db import models

# Create your models here.
from django.contrib.auth.models import  User,AbstractUser

class Korisnik(AbstractUser):
    br_obj_vijesti=models.IntegerField(default=0)



class Vijest(models.Model):
    autor=models.ForeignKey(Korisnik,on_delete=models.CASCADE)
    naslov= models.CharField(max_length=50)
    sadrzaj= models.CharField(max_length=500)
    timestamp=models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table='Vijest'
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        ret= super(Vijest,self).save()
        self.autor.br_obj_vijesti+=1
        self.autor.save()
        return ret
class Komentar(models.Model):
    vijest = models.ForeignKey(Vijest, on_delete=models.CASCADE)
    autor=models.ForeignKey(Korisnik,on_delete=models.CASCADE)
    sadrzaj = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    class Meta:
        db_table='Komentar'




