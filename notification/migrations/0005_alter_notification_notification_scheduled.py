# Generated by Django 4.0.3 on 2022-03-17 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_notification_notification_scheduled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_scheduled',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
