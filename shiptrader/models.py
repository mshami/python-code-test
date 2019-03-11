# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models


class Starship(models.Model):
    starship_class = models.CharField(
        verbose_name=_('Starship Class'),
        max_length=255
    )
    starship_class_slug = models.SlugField(
        verbose_name=_('Starship Class Slug'),
        help_text=_(' It is used for ORM queryset')
    )
    manufacturer = models.CharField(
        verbose_name=_('Manufacturer'),
        max_length=255
    )
    length = models.CharField(
        verbose_name=_('Length'),
        max_length=255
    )
    hyperdrive_rating = models.CharField(
        verbose_name=_('Hyperdrive Rating'),
        max_length=255
    )
    cargo_capacity = models.CharField(
        verbose_name=_('Cargo Capacity'),
        max_length=255
    )
    crew = models.CharField(
        verbose_name=_('Crew'),
        max_length=255
    )
    passengers = models.CharField(
        verbose_name=_('Passengers'),
        max_length=255
    )

    def __str__(self):
        return "Starship_id {} manufacture by {}".format(self.id, self.manufacturer)


class Listing(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255
    )
    ship_type = models.ForeignKey(
        Starship,
        verbose_name=_('Ship Type'),
        related_name='listings'
    )
    price = models.CharField(
        verbose_name=_('Price'),
        max_length=255
    )
    enabled = models.BooleanField(
        verbose_name=_("Activate/Deactivate"),
        default=True
    )
    created = models.DateTimeField(
        verbose_name=_('Creation date/time'),
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name
