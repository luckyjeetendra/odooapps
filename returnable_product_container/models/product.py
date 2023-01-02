# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    is_container = fields.Boolean('Is a Container', default=False)
    