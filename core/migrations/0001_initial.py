# Generated by Django 3.2.13 on 2022-09-18 23:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('mines', models.IntegerField()),
                ('map', models.JSONField()),
                ('is_over', models.BooleanField(default=False)),
                ('is_won', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map', models.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maps', to='core.game')),
            ],
        ),
    ]
