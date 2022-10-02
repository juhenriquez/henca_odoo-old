from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_invoice_register_payment(self):
        return self.env['account.payment'].with_context(
            active_ids=self.ids,
            active_model='account.move',
            active_id=self.id,
            sent_email=True
        ).action_register_payment()


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    sent_email = fields.Boolean(
        default=False,
        copy=False,
        help="It indicates that the account payment has been sent.",
        string="Sent Email..?"
    )
    email_sended = fields.Boolean(
        default=False,
        copy=False,
    )

    def post(self):
        res = super(AccountPayment, self).post()
        temp_name = "mail_template_data_payment_receipt_send_with_invoice"
        template_id = self.env.ref("send_payment_by_email." + temp_name)
        for payment in self.filtered(lambda p: not p.email_sended):
            if self._context.get('send_mail', False) or payment.send_mail and template_id:
                template_id.send_mail(payment.id, force_send=True)
                payment.write({'email_sended': True})

        return res


class AccountPaymentRegister(models.Model):
    _inherit = 'account.payment.register'

    sent_email = fields.Boolean(
        default=False,
        copy=False,
        help="It indicates that the account payment has been sent.",
        string="Sent Email..?"
    )

    def get_payme_prepare_payment_valsnts_vals(self, invoices):
        res = super(AccountPaymentRegister, self)._prepare_payment_vals(invoices)
        res.update({'sent_email': self.sent_email})
        return res
