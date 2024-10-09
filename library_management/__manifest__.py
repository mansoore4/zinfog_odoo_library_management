# -*- coding: utf-8 -*-
{
    'name': "Library Management",
    'summary': "Manage library books",
    'category': 'Library',
    'version': '16.0.1',
    'author': "Mansoor",
    'license': "LGPL-3",
    'depends': ['base', 'sale_management'],
    'data': [
        'views/book_view.xml',
        'views/library_menu.xml',
        'views/sale_order_view.xml',
        'security/ir.model.access.csv',
        'report/report_sale_order_inherit.xml',
    ],
    'installable': True,
    'application': True,
}
