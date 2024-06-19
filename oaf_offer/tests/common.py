from odoo import fields
from odoo.tests.common import TransactionCase, HttpCase, tagged, Form


@tagged('post_install', '-at_install')
class OafTestingCommon(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(OafTestingCommon, cls).setUpClass()

        # Create user.
        user = cls.env['res.users'].create({
            'name': 'POS Test Manager!',
            'login': 'postman',
            'password': 'postman',
            'groups_id': [(6, 0, cls.env.user.groups_id.ids), (4, cls.env.ref('point_of_sale.group_pos_manager').id)],
        })
        user.partner_id.email = 'postman@test.com'

        cls.env = cls.env(user=user)
        cls.cr = cls.env.cr
