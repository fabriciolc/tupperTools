# Generated by Django 2.1.7 on 2019-04-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listsemana',
            name='id',
        ),
        migrations.AlterField(
            model_name='listsemana',
            name='semana',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
