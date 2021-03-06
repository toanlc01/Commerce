# Generated by Django 4.0 on 2022-01-01 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auction_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='category',
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('none', 'None'), ('book', 'Book'), ('computer', 'Computer'), ('car', 'Car')], default='none', max_length=32)),
                ('auction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='auctions.auction')),
            ],
        ),
    ]
