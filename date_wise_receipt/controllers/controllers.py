# -*- coding: utf-8 -*-
# from odoo import http


# class DateWiseReceipt(http.Controller):
#     @http.route('/date_wise_receipt/date_wise_receipt', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/date_wise_receipt/date_wise_receipt/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('date_wise_receipt.listing', {
#             'root': '/date_wise_receipt/date_wise_receipt',
#             'objects': http.request.env['date_wise_receipt.date_wise_receipt'].search([]),
#         })

#     @http.route('/date_wise_receipt/date_wise_receipt/objects/<model("date_wise_receipt.date_wise_receipt"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('date_wise_receipt.object', {
#             'object': obj
#         })
