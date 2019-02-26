# -*- coding: utf-8 -*-
{
    'name': "SIEMPRE",

    'summary': """
        Módulo de Indicadores Financieros para el Sistema Especializado en el Manejo de Planificación y Recursos Empresariales (SIEMPRE)""",

    'description': """
        Trabajo Especial de Grado del Br. Jairo Martínez para la Obtención del Titulo de Licenciado en Computación
    """,

    'author': "Jairo Martínez",
    'website': "http://www.siempresistemas.com/nueva/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Indicadores',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        
        'views/main.xml',
        'views/templates.xml',
        'views/liquidez.xml',
        'views/eficiencia.xml',
        'views/indicador.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}