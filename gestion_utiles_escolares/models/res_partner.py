from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    tipo_contacto_escolar = fields.Selection(
        [
            ("estudiante", "Estudiante"),
            ("apoderado", "Apoderado"),
            ("personal", "Personal de la institución"),
            ("institucion", "Institución educativa")
        ],
        string="Tipo de contacto escolar"
    )

    grado_escolar = fields.Selection(
        [
            ("inicial_3", "Inicial 3 años"),
            ("inicial_4", "Inicial 4 años"),
            ("inicial_5", "Inicial 5 años"),
            ("1er_grado", "1er grado"),
            ("2do_grado", "2do grado"),
            ("3er_grado", "3er grado"),
            ("4to_grado", "4to grado"),
            ("5to_grado", "5to grado"),
            ("6to_grado", "6to grado")
        ],
        string="Grado escolar"
    )

    apoderado_principal_id = fields.Many2one(
        "res.partner",
        string="Apoderado principal",
        domain="[('tipo_contacto_escolar', '=', 'apoderado')]"
    )

    apoderado_secundario_id = fields.Many2one(
        "res.partner",
        string="Apoderado secundario",
        domain="[('tipo_contacto_escolar', '=', 'apoderado')]"
    )
