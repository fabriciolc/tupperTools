# Generated by Django 2.1.7 on 2019-04-09 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liberadas', '0024_auto_20190329_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='caixa_fabrica',
            name='liberada_status',
            field=models.BooleanField(default=False),
        ),
    ]