# Generated by Django 4.0 on 2021-12-24 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auctionlisting_created_at_bid_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('none', 'None'), ('book', 'Book'), ('computer', 'Computer'), ('car', 'Car')], default='none', max_length=32)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_listing', to='auctions.user')),
            ],
        ),
        migrations.AlterField(
            model_name='bid',
            name='listing',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bid_listing', to='auctions.auction'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='listing',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='auctions.auction'),
        ),
        migrations.DeleteModel(
            name='auctionListing',
        ),
    ]