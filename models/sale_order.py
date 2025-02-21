from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    commitment_delivery_date = fields.Date(string="Delivery Date")
    measurement_date = fields.Date(string="Aufmass Datum")

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        invoice_vals.update({
            'commitment_delivery_date': self.commitment_delivery_date,
            'measurement_date': self.measurement_date,
        })
        return invoice_vals




# class AccountMove(models.Model):
#     _inherit = 'account.move'
#
#
#     commitment_delivery_date = fields.Date(
#         string="Delivery Date",
#         related="invoice_origin_id.commitment_delivery_date",
#         store=True
#     )
#     measurement_date = fields.Date(
#         string="Aufmaß Datum",
#         related="invoice_origin_id.measurement_date",
#         store=True
#     )
#
#     invoice_origin_id = fields.Many2one(
#         'sale.order',
#         compute="_compute_invoice_origin_id",
#         store=True,
#         string="Original Quotation"
#     )
#
#     def _compute_invoice_origin_id(self):
#         for move in self:
#             move.invoice_origin_id = self.env['sale.order'].search(
#                 [('name', '=', move.invoice_origin)], limit=1
#             ) or False


class AccountMove(models.Model):
    _inherit = 'account.move'

    commitment_delivery_date = fields.Date(string="Delivery Date")
    measurement_date = fields.Date(string="Aufmaß Datum")

