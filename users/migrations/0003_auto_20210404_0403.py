# Generated by Django 3.1.7 on 2021-04-04 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210404_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_profile',
            field=models.CharField(max_length=20, null=True),
        ),
    ]