# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StatePrenda(models.Model):
    _name = 'chicdress.state.dress'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char(string='Estado',required=True)
    active = fields.Boolean(string="Activo",default=True  )

class NewModule(models.Model):
    _inherit = 'product.template'

    status = fields.Many2one(comodel_name="chicdress.state.dress", string="status", required=False, )


