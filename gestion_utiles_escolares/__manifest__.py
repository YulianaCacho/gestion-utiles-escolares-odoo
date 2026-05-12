{
    "name": "Gestión de Útiles Escolares",
    "version": "1.0",
    "summary": "Adaptación de Odoo para la gestión de útiles escolares",
    "description": "Campos personalizados para estudiantes, apoderados, productos y recepciones de útiles escolares.",
    "author": "Equipo Taller Integrador I",
    "category": "Inventory",
    "depends": ["base", "contacts", "stock", "product"],
    "data": [
        "views/res_partner_views.xml",
        "views/product_template_views.xml",
        "views/stock_picking_views.xml"
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3"
}
