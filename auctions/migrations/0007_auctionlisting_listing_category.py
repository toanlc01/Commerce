# Generated by Django 4.0 on 2021-12-24 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_rename_bids_bid_rename_comments_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='listing_category',
            field=models.CharField(choices=[('book', 'Book'), ('computer', 'Computer'), ('car', 'Car')], default='None', max_length=32),
        ),
    ]
