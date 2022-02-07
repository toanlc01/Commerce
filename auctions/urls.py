from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create-listing", views.create_listing_view, name="createListing"),
    path("listing/<id>", views.listing_view, name="listing"),
    path("add-remove-watchlist/<id>", views.change_watchList_status,
         name="changeWatchListStatus"),
    path("place-bid/<auction_id>", views.placeBid, name="placeBid")
]
