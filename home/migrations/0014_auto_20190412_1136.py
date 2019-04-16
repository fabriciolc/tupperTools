# Generated by Django 2.1.7 on 2019-04-12 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_distrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='distrito',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grupo_distrito', to='home.Distrito'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='grupomae',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grupo_grupo', to='home.Grupo'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='sembaixa',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='semnomeacao',
            field=models.IntegerField(null=True),
        ),
    ]