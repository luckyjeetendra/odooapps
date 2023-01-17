# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"
    
    is_deposit_line = fields.Boolean(related='product_id.is_container', store=True)
    