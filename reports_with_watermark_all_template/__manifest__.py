# -*- coding: utf-8 -*-
# Part of AktivSoftware See LICENSE file for full copyright
# and licensing details.
{
    'name': "Reports with Watermark 2.0",
    'summary': """
            Generates reports with watermark as per the image uploaded.
             """,
    'description': """
        The module mainly works with the functionality of ading
        watermark to all pdf reports in Odoo.
    """,
    'author': "Aktiv Software",
    'website': "http://www.aktivsoftware.com",
    'license': 'AGPL-3',
    'price': 11.00,
    'currency': "EUR",
    'category': 'report',
    'version': '13.0.1.0.0',
    'depends': ['web'],
    'data': [
        'views/res_company_views.xml',
        'report/external_layout_template.xml',
        'report/background_layout_template.xml',
        'report/boxed_layout_template.xml',
        'report/clean_layout_template.xml',
    ],
    'images': [
        'static/description/banner.jpg',
    ],
    'auto_install': False,
    'installable': True,
    'application': False
}
