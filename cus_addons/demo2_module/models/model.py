from odoo import api, fields, models, _

class demoModel_2(models.Model):
    # _name="demo_module2"
    # _name = "demo.model"
    _inherit = "demo.model"


    first_name = fields.Char("First Name")
    last_name = fields.Char("Last Name")
    