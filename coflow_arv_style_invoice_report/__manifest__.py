# -*- coding: utf-8 -*-
{
    'name': "ARV Style Invoice Report",

    'summary': """
        Customized invoice report template based on the ARV Supply Solutions format.""",

    'description': """
        This module provides a new PDF report for customer invoices that mimics the design of the provided sample invoice.
    """,

    'author': "Coflow",
    'website': "https://coflow.com.tr",

    'category': 'Accounting/Accounting',
    'version': '17.0',
    'depends': ['account'],

    # always loaded
    'data': [
        'report/invoice_report_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    "license": "LGPL-3",
}
