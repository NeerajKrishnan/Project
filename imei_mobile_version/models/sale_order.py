from odoo import fields, models, api,_


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    imei_scan_id = fields.Many2one('imei.scan.sale.order')

    def action_imei_scan_sale_order(self):

        if self.imei_scan_id:
            pass
        else:
            self.imei_scan_id = self.imei_scan_id.sudo().create({'sale_order_id': self.id})
        view = self.env.ref('imei_mobile_version.imei_scan_sale_order_form_view')
        return {
            'name': _('Scan IMEI Numbers'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'imei.scan.sale.order',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id': self.imei_scan_id.id,
            'context': {'default_sale_order_id': self.id}
        }

