# -*- coding: utf-8 -*-

from odoo import models, fields, api, SUPERUSER_ID

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    # Override this function to create multiple Receipt for PO based on delivery date selected in POL.
    def _create_picking(self):
        StockPicking = self.env['stock.picking']
        for order in self.filtered(lambda po: po.state in ('purchase', 'done')):
            if any(product.type in ['product', 'consu'] for product in order.order_line.product_id):

                datalines = []
                for line in order.order_line:
                    data = self.env['purchase.order.line'].search([('order_id', '=', self.id), ('date_planned', '=', line.date_planned)])
                    if data not in datalines:
                        datalines.append(data)

                order = order.with_company(order.company_id)
                                
                for dline in datalines:
                    res = order._prepare_picking()
                    picking = StockPicking.with_user(SUPERUSER_ID).create(res)
                    moves = dline._create_stock_moves(picking)
                    moves = moves.filtered(lambda x: x.state not in ('done', 'cancel'))._action_confirm()
                    seq = 0

                    for move in sorted(moves, key=lambda move: move.date):
                        seq += 5
                        move.sequence = seq
                    moves._action_assign()
                    picking.message_post_with_view('mail.message_origin_link',
                        values={'self': picking, 'origin': order},
                        subtype_id=self.env.ref('mail.mt_note').id)
                    
        return True
