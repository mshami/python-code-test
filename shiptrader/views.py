# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from rest_framework import serializers, filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from shiptrader.models import Starship, Listing


class StarshipListingSerializer(serializers.ModelSerializer):

    manufacturer = serializers.CharField(
        source='ship_type.manufacturer',
        read_only=True
    )
    starship_class = serializers.CharField(
        source='ship_type.starship_class',
        read_only=True
    )
    starship_class_slug = serializers.CharField(
        source='ship_type.starship_class_slug',
        read_only=True
    )
    length = serializers.CharField(
        source='ship_type.length',
        read_only=True
    )
    hyperdrive_rating = serializers.CharField(
        source='ship_type.hyperdrive_rating',
        read_only=True
    )
    cargo_capacity = serializers.CharField(
        source='ship_type.cargo_capacity',
        read_only=True
    )
    crew = serializers.CharField(
        source='ship_type.crew',
        read_only=True
    )
    passengers = serializers.CharField(
        source='ship_type.passengers',
        read_only=True
    )
    created = serializers.DateTimeField(
        read_only=True
    )

    class Meta:
        model = Listing
        fields = (
            'id',
            'name',
            'price',
            'manufacturer',
            'starship_class',
            'starship_class_slug',
            'length',
            'hyperdrive_rating',
            'cargo_capacity',
            'crew',
            'passengers',
            'enabled',
            'created',
        )


class StarshipListing(generics.ListAPIView):

    queryset = Listing.objects.filter(enabled=True)
    serializer_class = StarshipListingSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('price', 'created')


class StarshipClassListing(APIView):

    def get(self, request, starship_class_slug):
        starship_class_listing = Listing.objects.filter(
            ship_type__starship_class_slug=starship_class_slug,
            enabled=True,
        )
        serializer = StarshipListingSerializer(starship_class_listing, many=True)
        return Response(serializer.data)


class StarshipDetails(generics.RetrieveUpdateAPIView):

    serializer_class = StarshipListingSerializer
    lookup_field = 'id'

    def get_object(self):
        id = self.kwargs["object_id"]
        return get_object_or_404(Listing, id=id)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
