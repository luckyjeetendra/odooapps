# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    def _remove_deposit_line(self):
        deposit_lines = self.env['purchase.order.line'].search([('order_id', 'in', self.ids), ('is_deposit', '=', True)])
        if not deposit_lines:
            return
        to_delete = deposit_lines.filtered(lambda x: x.qty_invoiced == 0)
        if not to_delete:
            raise UserError(
                _('You can not update the deposit costs on an order where it was already invoiced!\n\nThe following delivery lines (product, invoiced quantity and price) have already been processed:\n\n')
                + '\n'.join(['- %s: %s x %s' % (line.product_id.with_context(display_default_code=False).display_name, line.qty_invoiced, line.price_unit) for line in delivery_lines])
            )
        to_delete.unlink()


    def _get_deposit_lines(self):
        value_list = []
        for line in self.order_line:
            dep_line = self.env['deposit.line'].search([('uom_id', '=', line.product_uom.id), ('product_id', '=', line.product_id.id)])
            if dep_line:
                value = {
                    'order_id': self.id,
                    'name': dep_line.container_product_id.name,
                    'product_qty': line.product_qty,
                    'product_uom': dep_line.container_product_id.uom_id.id,
                    'product_id': dep_line.container_product_id.id,
                    'price_unit': dep_line.price_deposit,
                    'is_deposit': True,
                }
                value_list.append(value)

        return value_list


    def set_deposit_line(self):
        self._remove_deposit_line()
        for order in self:
            PurchaseOrderLine = self.env['purchase.order.line']            
            values = order._get_deposit_lines()
            # Create the purchase order line
            for val in values:
                if order.order_line:
                    val['sequence'] = order.order_line[-1].sequence + 1
                pol = PurchaseOrderLine.sudo().create(val)

        return True


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    is_deposit = fields.Boolean(string="Is a Deposit", default=False)