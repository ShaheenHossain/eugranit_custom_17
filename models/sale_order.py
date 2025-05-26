from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    external_partner_id = fields.Many2one('res.partner', string='External Customer')


    commitment_delivery_date = fields.Date(string="Delivery Date")
    measurement_date = fields.Date(string="Aufmass Datum")

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        invoice_vals.update({
            'commitment_delivery_date': self.commitment_delivery_date,
            'measurement_date': self.measurement_date,
        })
        return invoice_vals

    is_external_company = fields.Boolean(
        string="External Company",
        compute="_compute_is_external_company",
        store=True,  # ✅ Make sure the field is stored
        related='partner_id.is_external_company',
        readonly=True

    )



class AccountMove(models.Model):
    _inherit = 'account.move'

    commitment_delivery_date = fields.Date(string="Delivery Date")
    measurement_date = fields.Date(string="Aufmaß Datum")




class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_external_company = fields.Boolean(string="External Company")


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    commitment_delivery_date = fields.Datetime("Commitment Delivery Date")
    measurement_date = fields.Date(string="Aufmaß Datum")
