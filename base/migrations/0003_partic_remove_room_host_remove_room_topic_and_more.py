# Generated by Django 5.2.1 on 2025-06-29 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='partic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('password', models.TextField(max_length=125)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='host',
        ),
        migrations.RemoveField(
            model_name='room',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
