# Generated by Django 4.0 on 2022-01-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auction_category_auction_photo_auction_posted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
