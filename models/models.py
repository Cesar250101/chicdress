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

    status = fields.Many2one(comodel_name="chicdress.state.dress", string="status", required=False,default=1 )
    valor_garantia = fields.Integer(string="Garantia", required=False, )
    valor_comision = fields.Integer(string="Comisión", required=False, )

class NewModule(models.Model):
    _inherit = 'product.product'

    imagen_mediana = fields.Binary(string="Imagen", related="product_tmpl_id.image_medium" )

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    imagen_mediana = fields.Binary(string="Imagen", related="product_id.imagen_mediana" )

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    devolucion_date = fields.Date(string="Fecha Devolución", required=True, )


class Desapcho(models.Model):
    _inherit = 'stock.picking'
    fecha_ini = fields.Date(string="Fecha Inicial", required=False, )
    fecha_fin= fields.Date(string="Fecha Final", required=False, )

class LineasStock(models.Model):
    _inherit = 'stock.move'

    fecha_ini = fields.Date(string="Fecha Inicial",related="picking_id.fecha_ini" ,required=False, )
    fecha_fin = fields.Date(string="Fecha Final", related="picking_id.fecha_fin",required=False, )

class Proveedor(models.Model):
    _inherit = 'res.partner'

    product_ids = fields.One2many(comodel_name="product.supplierinfo", inverse_name="name", string="Productos", required=False, )