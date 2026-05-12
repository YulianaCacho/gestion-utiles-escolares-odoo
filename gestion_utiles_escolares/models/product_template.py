from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    tipo_uso_escolar = fields.Selection(
        [
            ("personal", "Útil personal"),
            ("material_comun", "Material común del colegio"),
            ("aula", "Material de aula"),
            ("aseo", "Material de aseo"),
            ("psicomotricidad", "Psicomotricidad"),
            ("no_inventariable", "No inventariable")
        ],
        string="Tipo de uso escolar",
        help="Clasifica el útil según el tratamiento que tendrá dentro del proceso escolar."
    )
