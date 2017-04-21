# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import sale
from . import milestone


def register():
    Pool.register(
        sale.Sale,
        milestone.Milestone,
        module='sale_project_invoice_milestone', type_='model')
