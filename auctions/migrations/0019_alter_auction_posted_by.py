# Generated by Django 4.0 on 2022-01-23 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_auction_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='posted_by',
            field=models.ForeignKey(default='Author not specified', on_delete=django.db.models.deletion.CASCADE, related_name='myAuction', to='auctions.user'),
        ),
    ]