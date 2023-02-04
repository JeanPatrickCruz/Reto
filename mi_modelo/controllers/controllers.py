# -*- coding: utf-8 -*-
# from odoo import http


# class MiModelo(http.Controller):
#     @http.route('/mi_modelo/mi_modelo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mi_modelo/mi_modelo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mi_modelo.listing', {
#             'root': '/mi_modelo/mi_modelo',
#             'objects': http.request.env['mi_modelo.mi_modelo'].search([]),
#         })

#     @http.route('/mi_modelo/mi_modelo/objects/<model("mi_modelo.mi_modelo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mi_modelo.object', {
#             'object': obj
#         })
