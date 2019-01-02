# -*- coding: utf-8 -*-

from odoo import models, fields

class CreditPartner(models.Model):
	_name = 'sales_mp.manufacture'

	name = fields.Char(string="Title", required=True)
