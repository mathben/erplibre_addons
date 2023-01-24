from odoo import _, api, fields, models


class DefiAliment(models.Model):
    _name = "defi.aliment"
    _description = "Défi aliment :-)"

    name = fields.Char(string="Nom de l'aliment")

    prix = fields.Integer(
        string="Prix de l'aliment",
        help="Ceci indique le prix de l'aliment :-)",
    )
