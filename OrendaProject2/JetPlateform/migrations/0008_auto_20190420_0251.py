# Generated by Django 2.1.4 on 2019-04-20 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JetPlateform', '0007_condidature_isaccepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cin',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='no image', upload_to=''),
        ),
    ]