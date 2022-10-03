
from odoo import fields, models, api, _


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    # l10n_do_dgii_payer_type = fields.Selection(
    #     related="partner_id.l10n_do_dgii_payer_type",
    #     string="Taxpayer Type",
    # )
    ncf_control = fields.Boolean(
        compute='check_ncf_control',
        store=True
    )

    @api.one
    @api.depends('template_id', 'template_id.journal_id', 'template_id.journal_id.l10n_latam_use_documents')
    def check_ncf_control(self):
        return True if self.template_id and self.template_id.journal_id.l10n_latam_use_documents else False

