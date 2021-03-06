# Generated by Django 4.0 on 2022-01-01 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_remove_auction_category_remove_auction_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[('none', 'None'), ('book', 'Book'), ('computer', 'Computer'), ('car', 'Car')], default='none', max_length=32),
        ),
        migrations.AddField(
            model_name='auction',
            name='photo',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='myAuction', to='auctions.user'),
        ),
    ]
