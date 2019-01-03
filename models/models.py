# -*- coding: utf-8 -*-

from odoo import models, fields


class Brand(models.Model):
	_name = 'sales.brand'
	_description = 'A model for a brand of mobile phone.'
	name = fields.Char(string="Brand_Name", required=True)
	model_id = fields.One2many('sales.model', 'brand_id')

class Model(models.Model):
	_name = 'sales.model'
	_description = 'A model for a model of mobile phone.'
	name = fields.Char(string="Model_Name", required=True)
	brand = fields.Char(related='brand_id.name', store='False', string='Brand_Of_Model')
	brand_id = fields.Many2one('sales.brand', ondelete='set null', string='Brands', required=True)


class Brand_Model_Product(models.Model):
	_inherit = 'product.template'
	choosen_brand = fields.Many2one('sales.brand', ondelete='set null', string='Brand', required=True)
	choosen_model = fields.Many2one('sales.model', ondelete='set null', string='Model', required=True)
