# Generated by Django 4.2.13 on 2024-07-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(default='training', max_length=254),
            preserve_default=False,
        ),
    ]