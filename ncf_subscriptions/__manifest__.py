{
    'name': "NCF Manager Support for Sale Subscriptions",
    'version': '15.0',
    'category': 'Subscription',
 
    'author': 'Marcus Almeida, Grupo Consultoria Henca',
    'license': 'AGPL-3',
    "depends" : [
        'sale_subscription',
        'l10n_do_accounting',
    ],
    'data': ["views.xml"],
    "installable": True
}
