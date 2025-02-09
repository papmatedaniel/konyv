from django.db import models

class Szerzok(models.Model):
    szerzo = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Szerzok"

    def __str__(self):
        return self.szerzo

class Mufajok(models.Model):
    mufaj = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Mufajok"

    def __str__(self):
        return self.mufaj

class Konyvek(models.Model):
    cim = models.CharField(max_length=100)
    szerzok = models.ManyToManyField(Szerzok, related_name="konyvek")
    mufajok = models.ManyToManyField(Mufajok, related_name="konyvek")
    kiadas_eve = models.CharField(max_length=20,blank=True)
    kiado = models.CharField(max_length=100, null=True, blank=True)
    nyelv = models.CharField(max_length=50, null=True, blank=True)
    oldalszam = models.CharField(max_length=20, blank=True)
    kotes_tipus = models.CharField(max_length=50, null=True, blank=True)
    leiras = models.TextField(null=True, blank=True)
    boritokep = models.ImageField(upload_to='borito_kepek/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Konyvek"

    def __str__(self):
        return self.cim