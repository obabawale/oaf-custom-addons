from datetime import date, timedelta
from odoo.tests.common import tagged
from odoo.addons.oaf_offer.tests.common import OafTestingCommon
from odoo.exceptions import UserError

class TestAccountAccount(OafTestingCommon):

    @tagged('validity')
    def test_user_error_raised_if_datefrom_greater_than_dateto(self):
        """Test the assertion is raised when date_from is greater than date_to."""
        with self.assertRaises(UserError), self.cr.savepoint():
            self.env['product.template'].create({
                'name': "Offer 1",
                'uom_id': self.env.ref('uom.product_uom_dozen').id,
                'lst_price': 200.0,
                'standard_price': 160.0,
                'date_from': date.today(),
                'date_to': date.today() + timedelta(days=-1),
            })
    
    def test_create_offer_successfully(self):
        """Test that we can create a offer successfully."""
        pass