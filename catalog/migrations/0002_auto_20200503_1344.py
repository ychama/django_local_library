# Generated by Django 3.0.5 on 2020-05-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter a book genre (e.g Science Fiction)', max_length=200),
        ),
    ]
