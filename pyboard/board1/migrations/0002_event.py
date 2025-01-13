# Generated by Django 5.1.4 on 2025-01-13 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]