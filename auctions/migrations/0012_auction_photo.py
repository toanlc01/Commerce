# Generated by Django 4.0 on 2021-12-24 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auction_alter_bid_listing_alter_comment_listing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
    ]