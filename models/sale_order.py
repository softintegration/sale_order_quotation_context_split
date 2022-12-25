# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    type = fields.Selection([('quotation','Quotation'),
                             ('sale','Sale')],string='Type')
    state_sale = fields.Selection(related='state',store=False)