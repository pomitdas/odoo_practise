from odoo import api, fields, models, _


class EstateModel(models.Model):
    _name = "estate.model"
    _description = "Estate Model"
    _rec_name = "title"


    title = fields.Char(string="Title",required=True,help="hElp string")
    property_type = fields.Char(string='property_type')
    postcode=fields.Integer(string='postcode')
    bedrooms=fields.Integer(string='bedrooms')
    living_area=fields.Float(string='living_area')

    offer=fields.Integer(string="offer")


    tab=fields.Char("Tab")
    tab1=fields.Char("Tab1")

    