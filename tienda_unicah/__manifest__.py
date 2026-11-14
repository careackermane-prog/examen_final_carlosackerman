
{
    "name": "Tienda UNICAH",
    "version": "1.0",
    "summary": "Convenios de descuento para la tienda universitaria",
    "category": "Sales/Sales",
    "author": "Carlos Eduardo Ackerman Espinoza",
    "depends": [
        "base",
        "sale_management",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/tienda_convenio_data.xml",
        "views/res_partner_views.xml",
        "views/tienda_convenio_views.xml",
        "views/sale_order_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": True,
}
