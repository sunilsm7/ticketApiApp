# Generated by Django 2.0.6 on 2018-07-03 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20180613_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
