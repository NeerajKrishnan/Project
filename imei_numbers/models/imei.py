# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class IMEI(models.Model):
    _name = "mis.imei"
    _description ='IMEI Details'
    _rec_name ='imei_number'

    imei_number = fields.Char(string='IMEI Number')
    company_id = fields.Many2one("res.company", "Company", required=True, default=lambda self: self.env.company)
    product_id = fields.Many2one(
        "product.product",
        "Product",
        ondelete="cascade",
    )
    status = fields.Selection([('Available', 'Available'), ('Sold', 'Sold')], default='Available', compute='_update_status')
    store = fields.Char(string="Store", default='', track_visibility='onchange', readonly=True)


    def _update_status(self):
        for rec in self:
            objimei = self.env['mis.imei.tracking'].search([('imei_number', '=', rec.id)], order='id desc', limit=1)
            rec.status = 'Available'
            rec.store = ''
            for rec_imei in objimei:
                rec.status='Sold'
                rec.store = rec_imei.location

    _sql_constraints = [
        ("name_uniq", "unique(imei_number)", "IMEI Number must be unique")
    ]

class IMEITracking(models.Model):
    _name = "mis.imei.tracking"
    _description ='IMEI Tracking Information'

    imei_number = fields.Many2one("mis.imei", string='IMEI Number', required=True)
    company_id = fields.Many2one("res.company", "Company", required=True, default=lambda self: self.env.company)
    product_id = fields.Many2one(
        "product.product",
        "Product",
        related='imei_number.product_id',
        ondelete="cascade",
        required=True,
    )
    location = fields.Char(string="Location", required=True, track_visibility='onchange')

    _sql_constraints = [
        ("name_uniq", "unique(imei_number)", "IMEI Number must be unique")
    ]

    # @api.depends('imei_number')
    # def _update_master(self):
    #     for rec in self:

