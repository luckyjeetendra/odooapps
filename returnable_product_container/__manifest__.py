# -*- coding: utf-8 -*-
{
    'name': "Returnable Product Container",

    'summary': """
        Returnable Product Container & Bottles""",

    'description': """
        This module can be used to collect deposit on Cans for water, soft drinks, beer, and other drinks and process refund of deposit against returned empty Cans.
    """,

    'author': "JKS",
    # 'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory/Purchase',
    'version': '15.0.2',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'purchase', 'account', 'sale_stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'data/data.xml',
        'views/product.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/saleorder.xml',
        'views/purchase.xml',
        'views/account.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
