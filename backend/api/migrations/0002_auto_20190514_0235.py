# Generated by Django 2.1.1 on 2019-05-13 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
