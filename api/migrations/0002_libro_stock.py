# Generated by Django 4.2.1 on 2023-05-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='stock',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
