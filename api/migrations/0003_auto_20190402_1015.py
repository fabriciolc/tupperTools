# Generated by Django 2.1.7 on 2019-04-02 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190402_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listsemana',
            name='semana',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='listsemana',
            name='idsemana',
            field=models.IntegerField(primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
