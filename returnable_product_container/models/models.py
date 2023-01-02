# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DepositLine(models.Model):
    _name = 'deposit.line'
    _description = 'Deposit on Products'
    _sql_constraints = [
        ('_unique_product_deposit', 'unique (uom_id, product_id)', "Two deposit for the same product is not allowed"),
    ]

    uom_id = fields.Many2one('uom.uom', string='UOM Reference', required=True, ondelete='cascade', index=True, copy=False)
    product_id = fields.Many2one(
        'product.product', string='Product', required=True,
        change_default=True, ondelete='restrict')
    container_product_id = fields.Many2one(
        'product.product', string='Container', required=True,
        change_default=True, ondelete='restrict', domain=[('is_container', '=', True)])
    price_deposit = fields.Float('Deposit Price', required=True, digits='Product Price', default=0.0)


class UoM(models.Model):
    _inherit = 'uom.uom'

    deposit_line = fields.One2many('deposit.line', 'uom_id', string='Deposit Lines', copy=True, auto_join=True)

