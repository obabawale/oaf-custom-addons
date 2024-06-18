# -*- coding: utf-8 -*-

from odoo import models, fields


class OafOffer(models.Model):
    _inherit = 'product.template'

    date_from = fields.Date('Validity')
    date_to = fields.Date('Date To')

