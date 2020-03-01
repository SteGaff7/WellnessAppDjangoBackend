from django.urls import path
from .views import ListSongsView, RestaurantList

urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('restaurants/', RestaurantList.as_view(), name="restaurants-all")
]
