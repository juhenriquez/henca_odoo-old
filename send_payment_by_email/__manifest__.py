{
    'name': 'send payment by email',
    'category': 'account',
    'version': '15.0',
    'summary': 'send payment by email',
    'description': """.""",
    'license': 'OPL-1',
    # Dependencies
    'external_dependencies': {
        'python': ["xlsxwriter"],
    },
    'depends': [
        'account',
    ],
    'data': [
        'data/payment_receipt_data.xml',
        'views/payment_view.xml',
    ],
    'author': 'Click',
    'maintainer': 'Click',
    'installable': True,
}
