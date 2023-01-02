# -*- coding: utf-8 -*-
{
    'name': "Returnable Product Container",

    'summary': """
        Returnable Product Container & Bottles""",

    'description': """
        Module to manage deposit products (product container) for glass bottles and large PET bottles.
        
        Examples:
        Pet Coca Cola 1,5L - € 0,25
        Bottle Heineken 0,33cl Deposit - € 0,15
        Crate 12 x 1,5L bottles - € 2,50
        Crate 24 x 0,33cl bottles - € 2,00
        Cask beer 50L - € 30,00
    """,

    'author': "JKS",
    # 'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory/Purchase',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'purchase', 'account'],

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
