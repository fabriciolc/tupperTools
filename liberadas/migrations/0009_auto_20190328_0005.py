# Generated by Django 2.1.7 on 2019-03-28 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liberadas', '0008_auto_20190328_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa_fabrica',
            name='codigo_caixa',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
