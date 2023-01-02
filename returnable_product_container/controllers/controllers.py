# -*- coding: utf-8 -*-
# from odoo import http


# class ReturnableProductContainer(http.Controller):
#     @http.route('/returnable_product_container/returnable_product_container', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/returnable_product_container/returnable_product_container/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('returnable_product_container.listing', {
#             'root': '/returnable_product_container/returnable_product_container',
#             'objects': http.request.env['returnable_product_container.returnable_product_container'].search([]),
#         })

#     @http.route('/returnable_product_container/returnable_product_container/objects/<model("returnable_product_container.returnable_product_container"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('returnable_product_container.object', {
#             'object': obj
#         })
