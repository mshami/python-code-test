from django.conf.urls import url

from shiptrader.views import StarshipListing, StarshipClassListing, StarshipDetails

urlpatterns = [
    url(r'^listing/', StarshipListing.as_view(), name='starship_listing'),
    url(r'^details/(?P<object_id>[0-9]+)$', StarshipDetails.as_view(), name='starship_details'),
    url(r'^starship-class/(?P<starship_class_slug>[-\w]+)$', StarshipClassListing.as_view(), name='starship_class'),
]
