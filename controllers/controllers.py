# -*- coding: utf-8 -*-
from odoo import http

# class Chicdress(http.Controller):
#     @http.route('/chicdress/chicdress/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chicdress/chicdress/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('chicdress.listing', {
#             'root': '/chicdress/chicdress',
#             'objects': http.request.env['chicdress.chicdress'].search([]),
#         })

#     @http.route('/chicdress/chicdress/objects/<model("chicdress.chicdress"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chicdress.object', {
#             'object': obj
#         })