# Generated by Django 2.1.4 on 2019-04-20 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JetPlateform', '0008_auto_20190420_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cin',
            field=models.IntegerField(blank=True),
        ),
    ]
