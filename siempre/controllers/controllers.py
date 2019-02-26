# -*- coding: utf-8 -*-
from odoo import http

# class Siempre(http.Controller):
#     @http.route('/siempre/siempre/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siempre/siempre/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siempre.listing', {
#             'root': '/siempre/siempre',
#             'objects': http.request.env['siempre.siempre'].search([]),
#         })

#     @http.route('/siempre/siempre/objects/<model("siempre.siempre"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siempre.object', {
#             'object': obj
#         })