# Generated by Django 2.1.7 on 2019-03-26 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ocorrencia',
            old_name='codigo_consultora',
            new_name='consultora',
        ),
    ]