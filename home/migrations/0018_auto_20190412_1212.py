# Generated by Django 2.1.7 on 2019-04-12 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20190412_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distrito',
            name='estado',
        ),
        migrations.AddField(
            model_name='distrito',
            name='semnomeacao',
            field=models.IntegerField(null=True),
        ),
    ]
