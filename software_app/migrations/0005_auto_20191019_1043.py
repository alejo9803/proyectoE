# Generated by Django 2.2.6 on 2019-10-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software_app', '0004_auto_20191019_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcion',
            name='descripcion',
            field=models.CharField(max_length=80),
        ),
    ]
