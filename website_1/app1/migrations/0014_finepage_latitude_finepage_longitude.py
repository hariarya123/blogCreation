# Generated by Django 4.2.4 on 2023-08-15 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_finepage_emg'),
    ]

    operations = [
        migrations.AddField(
            model_name='finepage',
            name='latitude',
            field=models.FloatField(default=17.384),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finepage',
            name='longitude',
            field=models.FloatField(default=78.4564),
            preserve_default=False,
        ),
    ]
