from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, related


class User(AbstractUser):
    pass


class Auction(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    photo = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="myAuction", null=True)
    watchList = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}'s price is ${self.price}"


class Comment(models.Model):
    comment = CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(
        Auction, on_delete=models.CASCADE, related_name="comment", default=None)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment", default=None)

    def __str__(self) -> str:
        return f"{self.user.username} comments {self.comment} on Auction {self.listing.name}."


class Bid(models.Model):
    bid = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(
        Auction, on_delete=models.CASCADE, related_name="bid_listing", default=None)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bid_listing", default=None)

    def __str__(self) -> str:
        return f"{self.user.username} bids ${self.bid} on Auction {self.listing.name}."


class Category(models.Model):
    CATEGORIES = (
        ('none', 'None'),
        ('book', 'Book'),
        ('computer', 'Computer'),
        ('car', 'Car')
    )
    category = models.CharField(
        max_length=32, choices=CATEGORIES, default="none")
    auction = models.ForeignKey(
        Auction, on_delete=models.CASCADE, related_name="category", null=True
    )

    def __str__(self) -> str:
        return f"Category: {self.category}"
