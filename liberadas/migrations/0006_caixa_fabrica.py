# Generated by Django 2.1.7 on 2019-03-28 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liberadas', '0005_liberada_semana_liberada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caixa_fabrica',
            fields=[
                ('codigo_caixa', models.IntegerField(primary_key=True, serialize=False)),
                ('lote', models.IntegerField()),
                ('volume_atual', models.IntegerField()),
                ('volume_total', models.IntegerField()),
                ('distribuicao', models.IntegerField()),
                ('rota', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('semana', models.IntegerField()),
                ('consultora', models.IntegerField()),
            ],
        ),
    ]
