# Generated by Django 4.2.6 on 2023-10-28 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='raport',
            name='description',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
