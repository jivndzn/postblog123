# Generated by Django 4.1.3 on 2022-11-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggerist', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=255),
        ),
    ]