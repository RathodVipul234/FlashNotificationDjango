# Generated by Django 4.0.3 on 2022-03-17 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_notification_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_notification_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
