# Generated by Django 2.1.7 on 2019-03-29 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('liberadas', '0021_auto_20190329_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liberada',
            name='id',
        ),
        migrations.AlterField(
            model_name='liberada',
            name='caixa_fabrica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='caixa_liberada', serialize=False, to='liberadas.Caixa_fabrica'),
        ),
    ]
