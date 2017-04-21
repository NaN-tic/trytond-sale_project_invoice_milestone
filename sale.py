# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Sale']


class Sale:
    __name__ = 'sale.sale'
    __metaclass__ = PoolMeta
    milestone_type = fields.Many2One(
        'project.invoice_milestone.type.group', 'Milestone Group Type',
        states={
            'readonly':  ~Eval('state').in_(['draft', 'quotation']),
            },
        depends=['parent_project'])

    def _get_project(self):
        project = super(Sale, self)._get_project()
        project.milestone_group_type = self.milestone_type
        return project
