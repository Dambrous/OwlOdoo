{
    # App information
    'name': 'Owl Addons',
    'version': '16.0.1.0.0',
    # 'category': 'Sale',
    # 'license': 'OPL-1',
    # Author
    'author': 'Dambrous',
    'maintainer': 'Dambrous',
    # Dependencies
    'depends': [
        'base',
        'contacts',
        'web',
        'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/owl_projects_views.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            # 'owl_addons/static/src/owl_addons.scss',
        ],
    },
}
