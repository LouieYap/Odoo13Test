# custom_code

from odoo import models, fields, api



class StockNotification(models.Model):
    _name = 'stock.warehouse.orderpoint'
    _inherit = 'stock.warehouse.orderpoint'

    @api.model
    def send_stock_notification(self):
        send_email = False
        for orderpoint in self.env['stock.warehouse.orderpoint'].search([]):
            if orderpoint.product_id.qty_available <= orderpoint.product_min_qty:
                send_email = True
                break
        if send_email:
                template_id = self.env.ref('custom_code.stock_notification_email_template').id
                template = self.env['mail.template'].browse(template_id)
                template.send_mail(self.env['stock.warehouse.orderpoint'].search([])[0].id, force_send = True)