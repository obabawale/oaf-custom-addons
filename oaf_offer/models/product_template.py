# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api
from odoo.exceptions import UserError

class OafOffer(models.Model):
    _inherit = 'product.template'

    date_from = fields.Date('Validity')
    date_to = fields.Date('Date To')

    @api.constrains('date_from', 'date_to')
    def _constrains_validity_period(self):
        if self.date_from and self.date_to and self.date_from > self.date_to:
            raise UserError("Invalid validity period set")
        
    @api.model
    def _cron_deactivate_expired_offer(self):
        """Get records to expire and expire them
        """
        domain_to_expire = [
            ('active', '=', True),
            ('date_from', '>=', date.today()),
            ('date_to', '<=', date.today()),
        ]
        records_to_expire = self.search(domain_to_expire)
        return records_to_expire.update({'active': False})

