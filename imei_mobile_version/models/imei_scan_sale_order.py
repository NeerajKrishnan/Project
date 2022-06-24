from odoo import fields, models, api,_
from odoo.exceptions import UserError

class MisImei(models.Model):
    _inherit  = 'mis.imei'
    imei_number = fields.Char(string='IMEI Number')
    imei_sale_order_id = fields.Many2one('imei.scan.sale.order')
    active = fields.Boolean(default=True)

class ImeiMobileVersion(models.Model):
    _name = 'imei.scan.sale.order'
    _description = 'Description'

    sale_order_id = fields.Many2one('sale.order')
    sale_order_line_id = fields.Many2one('sale.order.line')
    sale_id = fields.Integer(related='sale_order_id.id')
    # product_id_domain = fields.Char(
    #     compute="_compute_product_id_domain",
    #     readonly=True,
    #     store=False,
    # )
    product_id = fields.Many2one(related='sale_order_line_id.product_id',)
    imei_numbers = fields.One2many('mis.imei', 'imei_sale_order_id')
    product_qty = fields.Float(related='sale_order_line_id.product_uom_qty')


    @api.onchange('sale_order_line_id')
    def invisible_from_list(self):
        temp = self.imei_numbers.filtered(lambda m: m.product_id.id != self.sale_order_line_id.product_id.id)
        temp2 = self.imei_numbers.filtered(lambda m: m.product_id.id == self.sale_order_line_id.product_id.id)

        for rec in temp:
            rec.active = False
        for rec in temp2:
            rec.active = True

    @api.onchange('imei_numbers')
    def check_limit(self):
        temp = self.imei_numbers.filtered(lambda m: m.product_id.id == self.sale_order_line_id.product_id.id)

        if self.product_qty >= len(temp):
            pass
        else:
            raise UserError(_("Unable to find Wkhtmltopdf on this system. The PDF can not be created."))




    def generate_imei_number(self):
        temp = self.imei_numbers.filtered(lambda m: m.product_id.id == self.sale_order_line_id.product_id.id)
        if len(temp) == self.product_qty:
            pass
        else:
            self.env['mis.imei'].sudo().create({
                'product_id':self.sale_order_line_id.product_id.id,
                'imei_sale_order_id' : self.id,

            })
            
