# Generated by Django 4.2 on 2023-06-18 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_room_user1_alter_room_user2'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='last_chat_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]