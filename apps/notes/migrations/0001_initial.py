# Generated by Django 4.2.9 on 2024-03-06 15:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=228, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_checked', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
