# Generated by Django 5.2 on 2025-04-17 04:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('srno', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(blank=True, default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
