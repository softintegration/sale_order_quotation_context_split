# -*- coding: utf-8 -*-

{
    'name': 'Split-up the Quotation management from the Sale orders',
    'version': '1.0.1.2',
    'author':'Soft-integration',
    'category': 'Sale',
    'summary': 'Split-up the Quotation management from the Sale orders',
    'description': "",
    'depends': [
        'sale'
    ],
    'data': [
        'views/sale_views.xml',
        'report/sale_report_templates.xml',
        'report/sale_report.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
