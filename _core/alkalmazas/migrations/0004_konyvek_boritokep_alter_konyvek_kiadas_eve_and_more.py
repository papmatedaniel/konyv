# Generated by Django 5.1.5 on 2025-02-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alkalmazas', '0003_konyvek_kiadas_eve_konyvek_kiado_konyvek_kotes_tipus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='konyvek',
            name='boritokep',
            field=models.ImageField(blank=True, null=True, upload_to='borito_kepek/'),
        ),
        migrations.AlterField(
            model_name='konyvek',
            name='kiadas_eve',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='konyvek',
            name='oldalszam',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
