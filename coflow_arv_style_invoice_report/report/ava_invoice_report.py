# -*- coding: utf-8 -*-
from odoo import models

class ReportAvaInvoice(models.AbstractModel):
    _name = 'report.ava_style_invoice.ava_invoice_template'
    _description = 'AVA Style Invoice Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs,
        }