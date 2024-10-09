from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_reference = fields.Char('Customer Reference')

    def action_confirm(self):
        """Confirm the sale order and send a confirmation email to the customer."""
        # Call the original method to perform the confirmation
        res = super(SaleOrder, self).action_confirm()

        # Prepare the email template
        template_id = self.env.ref('sale.mail_template_sale_confirmation', raise_if_not_found=False)

        # Send email for confirmed order
        if template_id:
            for order in self:
                if order.state == 'sale':
                    template_id.send_mail(order.id, force_send=True)

        return res
