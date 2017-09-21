# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta, Pool
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
        depends=['state'])

    def _get_project(self):
        project = super(Sale, self)._get_project()
        if project:
            project.milestone_group_type = self.milestone_type
        return project

    @classmethod
    def create_projects(cls, sales):
        super(Sale, cls).create_projects(sales)
        pool = Pool()
        Work = pool.get('project.work')
        Milestone = pool.get('project.invoice_milestone')
        projects = set()
        for sale in sales:
            for line in sale.lines:
                if line.project:
                    projects.add(line.project)
        Work.create_milestone(projects)
        milestones = []
        for p in projects:
            milestones += p.milestones
        Milestone.confirm(milestones)
