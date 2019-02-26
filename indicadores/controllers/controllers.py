# -*- coding: utf-8 -*-
from odoo import http

# class Indicadores(http.Controller):
#     @http.route('/indicadores/indicadores/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/indicadores/indicadores/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('indicadores.listing', {
#             'root': '/indicadores/indicadores',
#             'objects': http.request.env['indicadores.indicadores'].search([]),
#         })

#     @http.route('/indicadores/indicadores/objects/<model("indicadores.indicadores"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('indicadores.object', {
#             'object': obj
#         })