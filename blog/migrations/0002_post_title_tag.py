# Generated by Django 4.2 on 2023-05-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Stay Tuned with Blog', max_length=255),
        ),
    ]