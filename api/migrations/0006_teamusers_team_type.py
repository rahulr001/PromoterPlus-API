# Generated by Django 2.2.3 on 2019-07-22 12:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamusers',
            name='team_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
