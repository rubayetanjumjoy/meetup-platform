# Generated by Django 4.2.5 on 2023-09-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_platform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
