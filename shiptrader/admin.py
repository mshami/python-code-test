# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from rangefilter.filter import DateRangeFilter

from models import Starship, Listing


class StarshipAdmin(admin.ModelAdmin):

    model = Starship
    list_display = (
        'starship_class',
        'starship_class_slug',
        'hyperdrive_rating',
        'manufacturer',
    )
    search_fields = [
        'id',
        'starship_class',
        'manufacturer',
    ]

    list_per_page = 50
    ordering = ['id']

    fieldsets = (
        (_('Details'), {
            'fields': (
                'starship_class',
                'manufacturer',
                'length',
                'hyperdrive_rating',
                'cargo_capacity',
                'crew',
                'passengers',
                'starship_class_slug',
            )
        }),
    )


admin.site.register(Starship, StarshipAdmin)


class ListingAdmin(admin.ModelAdmin):

    model = Listing
    list_display = (
        'name',
        'price',
        'enabled',
        'created',
    )
    search_fields = [
        'id',
        'name',
        'price',
        'created',
    ]
    list_filter = (
        ('created', DateRangeFilter),
        'enabled',
    )
    readonly_fields = (
        'created',
    )
    list_per_page = 50
    ordering = ['-created']

    fieldsets = (
        (_('Details'), {
            'fields': (
                'name',
                'price',
                'ship_type',
                'enabled',
            )
        }),
        (_('Created'), {
            'fields': (
                'created',
            )
        }),
    )


admin.site.register(Listing, ListingAdmin)
