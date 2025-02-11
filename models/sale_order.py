from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    commitment_delivery_date = fields.Date(string="Delivery Date")
    measurement_date = fields.Date(string="Aufmass Datum")


class AccountMove(models.Model):
    _inherit = 'account.move'

    commitment_delivery_date = fields.Date(string="Delivery Date")
    measurement_date = fields.Date(string="Aufmass Datum")

