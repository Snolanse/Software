# Generated by Django 2.0.2 on 2018-04-04 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startside', '0009_auto_20180404_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lanse',
            old_name='trykk',
            new_name='ltrykk',
        ),
        migrations.AddField(
            model_name='lanse',
            name='vtrykk',
            field=models.IntegerField(default=0),
        ),
    ]
