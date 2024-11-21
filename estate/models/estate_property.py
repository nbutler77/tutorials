# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from dateutil.relativedelta import relativedelta

from odoo import fields, models


class Property(models.Model):
    _name = "estate.property"
    _description = "Estate model for a Property"

    name = fields.Char(required=True, string="Title")
    description = fields.Text()
    postcode = fields.Char()
    date_availibility = fields.Date(
        default=fields.Date.today() + relativedelta(months=+3),
        copy=False,
        string="Available From"
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection(
        [("North", "North"), ("South", "South"), ("East", "East"), ("West", "West")]
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [
            ("New", "New"),
            ("Offer Received", "Offer Received"),
            ("Offer Accepted", "Offer Accepted"),
            ("Sold", "Sold"),
            ("Cancelled", "Cancelled"),
        ],
        default=("New", "New"),
    )
