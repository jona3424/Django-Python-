from django.db import models


class Autor(models.Model):
    korime = models.CharField(primary_key=True, max_length=30)
    lozinka = models.CharField(max_length=30)
    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=30)
    mail = models.CharField(max_length=50, blank=True, null=True)
    telefon = models.CharField(max_length=30, blank=True, null=True)
    admin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'autor'


class Vest(models.Model):
    naslov = models.CharField(max_length=50)
    sadrzaj = models.CharField(max_length=500)
    autor = models.ForeignKey(Autor, models.DO_NOTHING, db_column='autor')
    datum = models.DateField()

    class Meta:
        managed = False
        db_table = 'vest'

    def __str__(self):
        return "naslov: " +self.naslov +" sadrzaj" +self.sadrzaj;

class Komentar(models.Model):
    vest=models.ForeignKey(Vest,on_delete=models.RESTRICT)
    sadrzaj=models.CharField(max_length=500)
    autor=models.ForeignKey(Autor,on_delete=models.RESTRICT)

    class Meta:
        db_table = 'komentar'

    def __str__(self):
        return "vijest: " + self.vest.naslov + " sadrzaj: " + self.sadrzaj +" autor: "+self.autor.korime
