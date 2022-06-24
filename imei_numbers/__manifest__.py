# -*- coding: utf-8 -*-
{
    'name': "IMEI Numbers Tracking",
    'version': '14.0.1.0',
    'license': 'Other proprietary',
    'category': 'Inventory Management',
    'summary': """IMEI Numbers Tracking""",
    'description': """
        IMEI Numbers Tracking.
    """,
    'author': "Mindinfsys",
    'website': 'www.mindinfosys.com',
    'depends': [
        'sale',
        'product',
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/imei_view.xml',
    ],
    'installable': True,
    'application': False,
}
