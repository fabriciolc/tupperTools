# Generated by Django 2.1.7 on 2019-04-12 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20190412_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultora',
            old_name='ultimativa',
            new_name='ultisemativa',
        ),
    ]