# Generated by Django 3.0.3 on 2020-02-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_mp4',
            field=models.FileField(upload_to='user_mp4'),
        ),
    ]