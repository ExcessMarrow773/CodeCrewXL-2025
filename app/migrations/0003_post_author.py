# Generated by Django 5.2.4 on 2025-07-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_category_options_post_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='admin', max_length=100),
        ),
    ]
