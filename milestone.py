# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Milestone']


class Milestone:
    __name__ = 'project.invoice_milestone'
    __metaclass__ = PoolMeta

    def _get_invoice(self):
        invoice = super(Milestone, self)._get_invoice()

        # return payment term/type from first sale
        for sale in self.project.sales:
            if sale.payment_term:
                invoice.payment_term = sale.payment_term
            if hasattr(sale, 'payment_type') and sale.payment_type:
                invoice.payment_type = sale.payment_type
                if hasattr(invoice, 'bank_account'):
                    # reset bank account in case sale payment type is not
                    # same default invoice payment type and not has bank account
                    invoice.on_change_with_bank_account()
            break
        return invoice
