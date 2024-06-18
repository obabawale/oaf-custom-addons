# -*- coding: utf-8 -*-
{
    'name': "One Acre Fund Offers",

    'summary': "Offers Module Implementation",

    'description': """
Offers Module Implementation
=============================
One Acre Fund has been using the Odoo Point of Sale (PoS) module to perform sales in shops. The product manager for your team has requested that you add a module that allows for creation and configuration of offers. An offer is defined as a grouping of one or more products that are sold at a promotional price for a limited time.

Features include:
- Create an offer 
- Configure the offer to contain one or more products
- Set a price for the offer
- Set a date range that the offer is valid
- The Point of Sale module should display valid offers with their associated prices and allow them to be ordered (BONUS: The receipt shows not only the offer name, but also the list of products included in the offer).
    """,
    'license': "LGPL-3",

    'author': "Olalekan Babawale",
    'website': "https://obabawale.github.io",

    'category': 'Stock',
    'version': '0.1',

    'depends': ['product'],

    'data': [
        'data/offer_cron.xml',
        'data/offer_cron.xml',
        'views/product_template_views.xml',
    ],
}

