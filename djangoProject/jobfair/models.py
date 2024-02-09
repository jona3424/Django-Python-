from django.db import models


class FizickoLice(models.Model):
    korisnickoime = models.OneToOneField('Korisnik', models.DO_NOTHING, db_column='korisnickoime', primary_key=True)
    ime = models.CharField(max_length=32)
    prezime = models.CharField(max_length=32)
    indeks = models.IntegerField()
    datum_rodjenja = models.DateField()
    fakultet = models.CharField(max_length=32)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fizicko_lice'


class JeKonkurisalo(models.Model):
    id_aplikacije = models.AutoField(primary_key=True)
    konkurs = models.ForeignKey('Konkurs', models.DO_NOTHING, db_column='konkurs')
    korisnik = models.ForeignKey(FizickoLice, models.DO_NOTHING, db_column='korisnik')
    datum_aplikacije = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'je_konkurisalo'


class Kompetencije(models.Model):
    idskill = models.AutoField(primary_key=True)
    naziv_kompetencije = models.CharField(max_length=32)
    opis = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'kompetencije'


class Konkurs(models.Model):
    id_konkurs = models.AutoField(primary_key=True)
    naziv = models.CharField(max_length=64)
    korisnickoime_komp = models.ForeignKey('PravnoLice', models.DO_NOTHING, db_column='korisnickoime_komp')
    broj_pozicija = models.IntegerField()
    datum_otvaranja = models.DateField()
    datum_zatvaranja = models.DateField()
    broj_godina_iskustva = models.IntegerField(blank=True, null=True)
    tip = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'konkurs'


class Korisnik(models.Model):
    korisnickoime = models.CharField(primary_key=True, max_length=32)
    lozinka = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'korisnik'


class PravnoLice(models.Model):
    korisnickoime = models.OneToOneField(Korisnik, models.DO_NOTHING, db_column='korisnickoime', primary_key=True)
    naziv = models.CharField(max_length=64)
    grad = models.CharField(max_length=32)
    pttbroj = models.IntegerField()
    adresa = models.CharField(max_length=32)
    pib = models.IntegerField(db_column='PIB')  # Field name made lowercase.
    direktor = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'pravno_lice'


class Racun(models.Model):
    brojracuna = models.CharField(primary_key=True, max_length=32)
    banka = models.CharField(max_length=32)
    kompanija = models.ForeignKey(PravnoLice, models.DO_NOTHING, db_column='kompanija')
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'racun'


class Zahtijeva(models.Model):
    konkurs = models.OneToOneField(Konkurs, models.DO_NOTHING, db_column='konkurs', primary_key=True)
    # The composite primary key (konkurs, kompetencija) found, that is not supported. The first column is selected.
    kompetencija = models.ForeignKey(Kompetencije, models.DO_NOTHING, db_column='kompetencija')

    class Meta:
        managed = False
        db_table = 'zahtijeva'
        unique_together = (('konkurs', 'kompetencija'),)


class Zaposleni(models.Model):
    id_zaposlenog = models.AutoField(primary_key=True)
    osoba_username = models.ForeignKey(FizickoLice, models.DO_NOTHING, db_column='osoba_username')
    kompanija_username = models.ForeignKey(PravnoLice, models.DO_NOTHING, db_column='kompanija_username')

    class Meta:
        managed = False
        db_table = 'zaposleni'
