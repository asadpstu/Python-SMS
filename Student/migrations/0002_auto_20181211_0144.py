# Generated by Django 2.1.4 on 2018-12-10 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='class_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.CharField(blank=True, max_length=210, null=True),
        ),
    ]
