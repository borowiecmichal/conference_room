# Generated by Django 3.1.6 on 2021-02-17 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_app', '0003_reservation_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['date']},
        ),
    ]