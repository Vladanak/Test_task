# -*- coding: utf-8 -*-
from odoo import http

# class SalesMp(http.Controller):
#     @http.route('/sales__mp/sales__mp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales__mp/sales__mp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales__mp.listing', {
#             'root': '/sales__mp/sales__mp',
#             'objects': http.request.env['sales__mp.sales__mp'].search([]),
#         })

#     @http.route('/sales__mp/sales__mp/objects/<model("sales__mp.sales__mp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales__mp.object', {
#             'object': obj
#         })