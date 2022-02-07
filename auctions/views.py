from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.utils import Error
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from auctions.models import Category, Auction, Bid

from .models import User

CATEGORIES = Category.objects.all()[0].CATEGORIES


def index(request):
    auctions = Auction.objects.all()
    return render(request, "auctions/index.html", {
        'auctions': auctions
    })


def listing_view(request, id):
    try:
        auction = Auction.objects.get(pk=id)
        noBid = len(auction.bid_listing.all())
        if noBid > 0:
            currentBid = auction.bid_listing.all().order_by('-bid')[0].bid
        else:
            currentBid = auction.price
    except:
        auction = False
        noBid = 0
    return render(request, "auctions/listing.html", {
        "auction": auction,
        "is_authenticated": request.user.is_authenticated,
        "watchList": auction.watchList,
        "numberOfBid": noBid,
        "currentBid": currentBid
    })


def change_watchList_status(request, id):
    auction = Auction.objects.get(pk=id)
    auction.watchList = not auction.watchList
    auction.save()
    return HttpResponseRedirect(reverse(listing_view, args=[id]))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def placeBid(request, auction_id):
    bid = request.POST["bid"]
    allBids = Auction.objects.get(pk=auction_id).bid_listing.all()
    for existingBid in allBids:
        if existingBid.bid > int(bid):
            messages.add_message(
                request, messages.INFO, 'The bid has to be greater than the current bid.')
            return HttpResponseRedirect(reverse(listing_view, args=[auction_id]))
    newBid = Bid(bid=bid, listing=Auction.objects.get(
        pk=auction_id), user=request.user)
    newBid.save()
    return HttpResponseRedirect(reverse(listing_view, args=[auction_id]))


def create_listing_view(request):
    if request.method == "GET":
        return render(request, "auctions/create_listing.html", {
            "categories": CATEGORIES
        })

    name = request.POST['name']
    description = request.POST['description']
    price = request.POST['startingBid']
    urlPhoto = request.POST['photo']
    category = request.POST['category']

    auction = Auction(name=name, description=description,
                      price=price, photo=urlPhoto, posted_by=request.user)
    auction.save()

    category = Category(category=category, auction=auction)
    category.save()

    return HttpResponse("auction created")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
