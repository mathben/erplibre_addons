from odoo import _, api, fields, models


class DefiAliment(models.Model):
    _name = "defi.aliment"
    _description = "demo_defi_aliment"

    name = fields.Char(string="Nom de l'aliment")
