# Generated by Django 2.1.7 on 2019-04-12 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20190412_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultora',
            old_name='CEP',
            new_name='cep',
        ),
    ]
