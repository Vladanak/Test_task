# -*- coding: utf-8 -*-

from odoo import models, fields


class Brand(models.Model):
	_name = 'sales.brand'
	_description = 'A model for a brand of mobile phone.'
	name = fields.Char(string="Title", required=True)
	model_id = fields.Many2one('sales.model', ondelete='set null', string='model', required=True)



class Model(models.Model):
	_name = 'sales.model'
	_description = 'A model for a model of mobile phone.'
	name = fields.Char(string="Model", required=True)
	brand = fields.Char(related='brand_id.name', store='False', string='nu')
	brand_id = fields.One2many('sales.brand', 'model_id', string='info', required=True)

