# Generated by Django 2.1.4 on 2019-04-20 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JetPlateform', '0006_auto_20190420_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='condidature',
            name='isAccepted',
            field=models.BooleanField(default=False),
        ),
    ]