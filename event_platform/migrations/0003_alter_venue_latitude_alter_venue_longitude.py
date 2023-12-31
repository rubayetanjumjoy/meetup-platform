# Generated by Django 4.2.5 on 2023-09-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_platform', '0002_alter_event_event_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='latitude',
            field=models.DecimalField(decimal_places=15, max_digits=15),
        ),
        migrations.AlterField(
            model_name='venue',
            name='longitude',
            field=models.DecimalField(decimal_places=15, max_digits=15),
        ),
    ]
