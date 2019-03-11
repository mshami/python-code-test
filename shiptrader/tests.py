# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.urls import reverse
from django.utils.text import slugify
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from shiptrader.models import Starship, Listing
from shiptrader.views import StarshipListingSerializer


class TestAPI(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.starship_1 = Starship.objects.create(
            starship_class="Starfighter",
            manufacturer="Kuat Systems Engineering",
            length="8",
            hyperdrive_rating="1.0",
            cargo_capacity="60",
            crew="1",
            passengers="0",
            starship_class_slug=slugify("starfighters")
        )
        self.listing_1 = Listing.objects.create(
            name="Jedi starfighter",
            ship_type=self.starship_1,
            price="180000",
            created="2014-12-20T17:35:23.906000Z"
        )
        self.starship_2 = Starship.objects.create(
            starship_class="Starfighter",
            manufacturer="Kuat Systems Engineeringgg",
            length="88",
            hyperdrive_rating="2.0",
            cargo_capacity="60",
            crew="2",
            passengers="0",
            starship_class_slug=slugify("starfighter")
        )
        self.listing_2 = Listing.objects.create(
            name="Jedi starfighter",
            ship_type=self.starship_2,
            price="190000",
            created="2015-12-20T17:35:23.906000Z"
        )

    def test_listing_model_found(self):
        self.assertEqual(self.listing_1.__str__(), self.listing_1.name)

    def test_startship_model_found(self):
        self.assertEqual(self.starship_1.__str__(), "Starship_id {} manufacture by {}".format(
            self.starship_1.id, self.starship_1.manufacturer))

    def test_model_can_create_a_starship(self):
        count = Starship.objects.count()
        self.assertEqual(count, 2)

    def test_model_can_create_a_starship_listing(self):
        count = Listing.objects.count()
        self.assertEqual(count, 2)

    def test_api_can_get_starship_deatils(self):
        response = self.client.get(
            reverse('starship_details',
            kwargs={'object_id': self.starship_1.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_not_delete_starship_details(self):

        response = self.client.delete(
            reverse('starship_details', kwargs={'object_id': self.starship_1.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_can_get_a_starship_listing(self):
        response = self.client.get(reverse('starship_listing'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_get_a_starship_class_listing(self):
        response = self.client.get('/shiptrader/starship-class/starfighter')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_starship_listing_serializer(self):
        response = self.client.get(reverse('starship_listing'))
        starship_listing = Listing.objects.filter(enabled=True)
        serialized = StarshipListingSerializer(starship_listing, many=True)
        self.assertEqual(response.data, serialized.data)

