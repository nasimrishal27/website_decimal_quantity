# -*- coding: utf-8 -*-
{
    'name': "Website decimal quantity",
    'version': '1.0',
    'depends': ['base', 'website_sale', 'sale'],
    'author': "Suni",
    'description': """
    POS Session Wise Discount
    """,
    # data files always loaded at installation
    'data': [
    ],
    "assets": {
        'web.assets_frontend': [
            "website_decimal_quantity/static/src/js/website_decimal_quantity.js",
            "website_decimal_quantity/static/src/js/quantity_buttons.js",
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',
}

