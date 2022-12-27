# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class StockPackageLevel(models.Model):
    _inherit = 'stock.package_level'

    purchase_order_id = fields.Many2one('purchase.order',related='package_id.purchase_order_id',
                                        string='Purchase order reference',store=True)

    

