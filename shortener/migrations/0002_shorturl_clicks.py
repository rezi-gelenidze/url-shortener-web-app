# Generated by Django 3.2.3 on 2021-05-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='clicks',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
