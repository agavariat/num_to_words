# -*- coding: utf-8 -*-

from num2words import num2words
from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    text_amount = fields.Char(string="Montant en lettre", required=False, compute="amount_to_words" )

    @api.multi
    @api.depends('amount_total')
    def amount_to_words(self):
        for record in self:
            if record.company_id.text_amount_language_currency:
               record.text_amount = num2words(record.amount_total, to='currency',
                                             lang=record.company_id.text_amount_language_currency)