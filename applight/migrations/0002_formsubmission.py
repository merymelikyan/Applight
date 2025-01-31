# Generated by Django 4.2 on 2025-01-18 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
