# Generated by Django 4.0 on 2021-12-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auction_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='photo',
            field=models.URLField(blank=True, null=True),
        ),
    ]