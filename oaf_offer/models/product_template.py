# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class OafOffer(models.Model):
    _inherit = 'product.template'

    date_from = fields.Date('Validity')
    date_to = fields.Date('Date To')
    is_offer = fields.Boolean('Is Offer')

    @api.constrains('date_from', 'date_to')
    def _constrains_validity_period(self):
        if self.date_from and self.date_to and self.date_from > self.date_to:
            raise UserError("Invalid validity period set")

    @api.model
    def _cron_deactivate_expired_offer(self):
        """Get records to expire and expire them
        """
        td = date.today()
        domain_to_expire = [
            ('active', '=', True),
            ('detailed_type', '=', 'combo'),
            ('date_from', '<=', td),
            ('date_to', '<', td),
        ]
        offers_to_expire = self.search(domain_to_expire)
        _logger.info(f"***** Offers to expire &&&& {offers_to_expire} *****")
        return offers_to_expire.update({'active': False})
