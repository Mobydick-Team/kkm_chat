# Generated by Django 4.2 on 2023-05-15 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.IntegerField()),
                ('user2', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_chat', models.DateTimeField(null=True)),
                ('last_sender', models.IntegerField(null=True)),
                ('unread_chat', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-last_chat'],
                'unique_together': {('user1', 'user2')},
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_id', models.IntegerField()),
                ('content', models.CharField(max_length=100)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=100)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.room')),
            ],
            options={
                'ordering': ['sent_at'],
            },
        ),
    ]
