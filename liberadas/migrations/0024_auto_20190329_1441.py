# Generated by Django 2.1.7 on 2019-03-29 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('liberadas', '0023_auto_20190329_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liberada',
            name='caixa_fabrica',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='caixa_liberada', serialize=False, to='liberadas.Caixa_fabrica'),
        ),
    ]
