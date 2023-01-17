# -*- coding: utf-8 -*-
{
    'name': "Returnable Product Container",

    'summary': """
        Returnable Product Container & Bottles""",

    'description': """
        This module can be used to collect deposit on Cans for water, soft drinks, beer, and other drinks and process refund of deposit against returned empty Cans.
    """,

    'author': "JKS",
    
    # Categories can be used to filter modules in modules listing
    'category': 'Inventory/Purchase',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'purchase', 'account', 'sale_stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product.xml',
        'views/views.xml',
        'views/saleorder.xml',
        'views/purchase.xml',
        'views/account.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
