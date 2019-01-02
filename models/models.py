# -*- coding: utf-8 -*-

from odoo import models, fields

class Manufactory(models.Model):
	_name = 'sales__mp.manufactory'
	_description = 'a model for a conference'
	name = fields.Char(string="Title", required=True)
