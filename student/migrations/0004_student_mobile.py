# Generated by Django 3.0.5 on 2022-11-07 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20221104_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]