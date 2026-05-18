from odoo import api, models, fields
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    tipo_uso_escolar = fields.Selection(
    [
        ("personal", "Útil personal"),
        ("material_comun", "Material común del colegio"),
        ("aula", "Material de aula"),
        ("manualidades", "Manualidades"),
        ("aseo", "Material de aseo"),
        ("psicomotricidad", "Psicomotricidad"),
        ("no_inventariable", "No inventariable")
    ],
    string="Tipo de uso escolar",
    help="Clasifica el útil según el tratamiento que tendrá dentro del proceso escolar."
)

    responsable_escolar_ids = fields.Many2many(
        "res.users",
        string="Responsables"
    )

    @api.constrains("responsable_escolar_ids")
    def _check_responsable_escolar_ids(self):
        for product in self:
            if len(product.responsable_escolar_ids) > 3:
                raise ValidationError("Solo se pueden seleccionar hasta 3 responsables.")