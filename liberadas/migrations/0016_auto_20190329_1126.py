# Generated by Django 2.1.7 on 2019-03-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liberadas', '0015_auto_20190329_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liberada',
            name='entregador',
            field=models.CharField(max_length=50),
        ),
    ]
